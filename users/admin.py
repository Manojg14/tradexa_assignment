from django.contrib import admin
from .models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_per_page = 25

    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = 'Full Name'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_text', 'created_at', 'updated_at')
    search_fields = ('user__username', 'text')
    list_filter = ('created_at',)
    list_per_page = 25

    def short_text(self, obj):
        return obj.text[:60] + '...' if len(obj.text) > 60 else obj.text
    short_text.short_description = 'Text Preview'
