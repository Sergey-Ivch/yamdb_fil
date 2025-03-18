from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Comment, Genre, GenreTitle, Review, Title, User


class CategoryResource(resources.ModelResource):
    # Создаем ресурс экспорта и импорта, наследуемся от ModelResource

    class Meta:
        model = Category
        fields = ('name', 'slug',)


class CategoryAdmin(ImportExportModelAdmin):
    # Создаем админку с добавлением интерфейса для экспорта и импорта
    # админку наследуем от ImportExportModelAdmin
    # определяем resources_class куда передаем наш ресурс, созданный ранее
    resources_class = CategoryResource
    list_display = ('id', 'name', 'slug')


admin.site.register(Category, CategoryAdmin)
# регистрируем админку


class TitleResource(resources.ModelResource):
    # Создаем ресурс экспорта и импорта, наследуемся от ModelResource

    class Mete:
        model = Title
        fields = ('name', 'year', 'category')


class TitlesAdmin(ImportExportModelAdmin):
    # Создаем админку с добавлением интерфейса для экспорта и импорта
    # админку наследуем от ImportExportModelAdmin
    # определяем resources_class куда передаем наш ресурс, созданный ранее
    resources_class = TitleResource
    list_display = ('id', 'name', 'year', 'category')


admin.site.register(Title, TitlesAdmin)
# регистрируем админку


class GenreResource(resources.ModelResource):
    # Создаем ресурс экспорта и импорта, наследуемся от ModelResource

    class Meta:
        model = Genre
        fields = ('name', 'slug',)


class GenreAdmin(ImportExportModelAdmin):
    # Создаем админку с добавлением интерфейса для экспорта и импорта
    # админку наследуем от ImportExportModelAdmin
    # определяем resources_class куда передаем наш ресурс, созданный ранее
    resources_class = GenreResource
    list_display = ('id', 'name', 'slug')


admin.site.register(Genre, GenreAdmin)
# регистрируем админку


class TitlesGenreResource(resources.ModelResource):
    # Создаем ресурс экспорта и импорта, наследуемся от ModelResource
    class Meta:
        model = GenreTitle
        fields = ('title_id', 'genre_id',)


class TitlesGenreAdmin(ImportExportModelAdmin):
    # Создаем админку с добавлением интерфейса для экспорта и импорта
    # админку наследуем от ImportExportModelAdmin
    # определяем resources_class куда передаем наш ресурс, созданный ранее
    resources_class = TitlesGenreResource
    list_display = ('title_id', 'genre_id')


admin.site.register(GenreTitle, TitlesGenreAdmin)
# регистрируем админку


admin.site.register(User)


class ReviewResource(resources.ModelResource):
    # Создаем ресурс экспорта и импорта, наследуемся от ModelResource

    class Meta:
        model = Review
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date',
                  'rating')


class ReviewAdmin(ImportExportModelAdmin):
    # Создаем админку с добавлением интерфейса для экспорта и импорта
    # админку наследуем от ImportExportModelAdmin
    # определяем resources_class куда передаем наш ресурс, созданный ранее
    resources_class = ReviewResource
    list_display = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')


admin.site.register(Review, ReviewAdmin)


class CommentResource(resources.ModelResource):
    # Создаем ресурс экспорта и импорта, наследуемся от ModelResource

    class Meta:
        model = Comment
        fields = ('title', 'text', 'author', 'score', 'pub_date',
                  'rating')


class CommentsAdmin(ImportExportModelAdmin):
    # Создаем админку с добавлением интерфейса для экспорта и импорта
    # админку наследуем от ImportExportModelAdmin
    # определяем resources_class куда передаем наш ресурс, созданный ранее
    resources_class = CommentResource
    list_display = ('id', 'pub_date', 'review', 'text', 'author')


admin.site.register(Comment, CommentsAdmin)


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'bio',
                  'first_name', 'last_name')


class UserAdmin(ImportExportModelAdmin):
    resources_class = UserResource
    list_display = ('id', 'username', 'email', 'role', 'bio',
                    'first_name', 'last_name')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
