import datetime as dt

from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator
from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title, User)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UnicodeUsernameValidator(),
            UniqueValidator(queryset=User.objects.all())
        ],
        max_length=150,
        required=True,
    )
    email = serializers.EmailField(
        max_length=254,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'bio',
                  'first_name', 'last_name')


class RegisterDataSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=[
            UnicodeUsernameValidator(),
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    email = serializers.EmailField(
        max_length=254,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Username me is not valid')
        return value

    class Meta:
        fields = ('username', 'email')
        model = User


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class UserEditSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=[
            UnicodeUsernameValidator(),
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Cattegory."""

    class Meta:
        fields = ('name', 'slug',)
        model = Category


class GenreTitleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre."""

    class Meta:
        fields = ('name', 'slug')
        model = GenreTitle


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre."""

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitlesSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Titles."""
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',)
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True)

    class Meta:
        fields = ('__all__')
        model = Title

    def validate_year(self, value):
        """Валидатор для проверки актуальности вводимого года произведения."""

        year = dt.date.today().year
        if year < value:
            raise serializers.ValidationError(
                'Проверьте год выхода произведения.'
            )
        return value


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review."""
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )

    def validate_score(self, value):
        """Валидатор для проверки значения оценки."""
        if not 1 <= value <= 10:
            raise serializers.ValidationError(
                'Оценкой может быть только целое число от 1 до 10.'
            )
        return value

    def validate(self, data):
        """Валидатор для проверки на ранее оствавленный отзыв"""
        author = self.context['request'].user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        if self.context['request'].method == 'POST':
            if Review.objects.filter(author=author, title=title).exists():
                raise serializers.ValidationError(
                    'На произведение можно оставить только один отзыв.')
        return data

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'


class ReadOnlyTitleSerializer(serializers.ModelSerializer):
    """Серилизатор для модели Title для не безопастных запросов."""
    rating = serializers.IntegerField(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'
