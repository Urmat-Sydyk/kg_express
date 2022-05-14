from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ListDisplay = ['name', 'slug', 'id']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    ListDisplay = (
        'name',
        'category',
        'slug',
        'id'
    )
    prepopulated_fields = {'slug':('name',)}
    list_filter = (
        "category",
    )
    search_fields = (
        'id',
        'name',
    )



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ListDisplay = [
        'name',
        'price',
        'image',
        'category',
        'subcategory',
        'created',
        'updated',
        'is_active',

    ]

@admin.register(BanerImage)
class BanerImageAdmin(admin.ModelAdmin):
    ListDisplay = ['name', 'add_link', 'image', 'created']
    list_filter = ['created']