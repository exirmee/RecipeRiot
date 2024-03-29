from django.contrib import admin
from.models import RecipeCats,Recipe,Units,ParentCats,RecipeReview

# Register your models here.
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','desc','image','parent_categories')

class RecipeAdmin(admin.ModelAdmin):
    list_display=('name','date','difficulty','timetoprepare')

class unitsAdmin(admin.ModelAdmin):
    list_display=('name','sign')
class parentCatsAdmin(admin.ModelAdmin):
    list_display=('name','description','image')

class reviewAdmin(admin.ModelAdmin):
    list_display=('recipe','user','review','rating','status')

admin.site.register(ParentCats,parentCatsAdmin)
admin.site.register(Units,unitsAdmin)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(RecipeCats,RecipeCategoryAdmin)
admin.site.register(RecipeReview,reviewAdmin)
