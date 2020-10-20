from django.contrib import admin
from .models import Academy,Sports,Coach

# admin.site.register(Academy)
# admin.site.register(Coach)
# admin.site.register(Sports)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('academy', 'name', 'exp')
    list_filter = ('academy', 'exp')
    #fields = ['academy', 'name', ('exp')]

@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'desc')
    list_filter = ('name', 'start_time')

@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    list_display = ('academy', 'sports_name', 'sports_type')
    list_filter = ('academy', 'sports_type')