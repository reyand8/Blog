from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ReviewType, Category, TagReview, Review



class ReviewTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    list_display_links = ('id', 'tag')
    search_fields = ('tag',)
    prepopulated_fields = {"slug": ("tag",)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'images', 'category', 'is_published', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text', 'tags', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(ReviewType, ReviewTypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TagReview, TagAdmin)
admin.site.register(Review, ReviewAdmin)
