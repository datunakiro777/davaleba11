from django.contrib import admin
from shop.models import Category, Tag, Item

class ItemInline(admin.TabularInline0):
    model = Item

class CategoryManager(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']
    inlines = [ItemInline]

class TagInLine(admin.StackedInline):
    model = Tag

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description']
    search_fields = ['name', 'description']
    ordering = ['-price']
    inlines = [TagInLine]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']