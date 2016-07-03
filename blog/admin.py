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
    list_display = ['title', 'get_author_nick', 'get_categories', 'pretty_created_at']
    fields = ['author', 'title', 'slug', 'content', 'categories']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

    def get_author_nick(self, obj):
        return obj.author.nickname
    get_author_nick.short_description = 'written as'

    def get_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all())
    get_categories.short_description = 'categories'

    def pretty_created_at(self, obj):
        return obj.created_at.strftime('%c')
    pretty_created_at.short_description = 'Created at'
