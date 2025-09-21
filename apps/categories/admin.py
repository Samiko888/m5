from django.contrib import admin

# Register your models here.
from apps.categories.models import Categories

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_dicplay = ('name')

   

