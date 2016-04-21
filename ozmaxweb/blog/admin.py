from django.contrib import admin

from .models import Author, Category, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'user']
    fields = ['user', 'nickname']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_user', 'get_author_nick', 'get_categories', ]
    fields = ['author', 'title', 'slug', 'content', 'categories']
    prepopulated_fields = {'slug': ('title',)}

    def get_user(self, obj):
        return obj.author.user.username
    get_user.short_description = 'User'

    def get_author_nick(self, obj):
        return obj.author.nickname
    get_author_nick.short_description = 'wrote as'

    def get_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all())
    get_categories.short_description = 'categories'
