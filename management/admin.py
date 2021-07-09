from django.contrib import admin

from .models import Profile, Author, Book, Publisher




class BookAdmin(admin.ModelAdmin):
    """ customizing book model in admin panel """

    list_display = ('id', 'title', 'page_number')
    list_display_links = ('title', 'id')
    list_filter = ('author', 'publisher__name')
    search_fields = ('title',)
    list_per_page = 25


class AuthorAdmin(admin.ModelAdmin):
    """ customizing author model in admin panel """

    list_display = ('id', 'first_name', 'last_name', 'nickname')
    list_display_links = ('id',)
    search_fields = ('first_name', 'last_name', 'nickname')
    list_per_page = 25


class PublisherAdmin(admin.ModelAdmin):
    """ customizing publisher model in admin panel """
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Profile,)