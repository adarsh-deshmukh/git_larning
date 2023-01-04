from django.contrib import admin
from .models import Position,employee

# Register your models here.
class PositionAdmin(admin.ModelAdmin):
    list_display=["title"]
class employeeAdmin(admin.ModelAdmin):
    list_display=["fullname","emp_code","mobile","position"]
admin.site.register(Position,PositionAdmin)
admin.site.register(employee)