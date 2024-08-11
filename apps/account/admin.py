from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline

from apps.account.models import Feed, Blog, Account


class BlogInline(TabularInline):
    model = Blog
    extra = 1

class FeedInline(admin.TabularInline):
    model = Feed
    extra = 1

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_filter = ("role",)
    list_display = ("first_name", "last_name", "username", 'role')
    list_display_links = ("username", 'role')
    search_fields = ("username", "first_name", 'role')
    date_hierarchy = "created_at"
    inlines = [FeedInline, BlogInline]


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_filter = ('name', 'body', 'account')
    list_display = ('name', 'body', 'account', 'website')
    list_display_links = ('name', 'body', 'account')

    search_fields = ('name', 'body', 'account')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_filter = ('title', 'body', 'owner')
    list_display = ('title', 'body', 'owner')
    list_display_links = ('title', 'body', 'owner')

    search_fields = ('title', 'body', 'owner')



