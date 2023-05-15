from django.contrib import admin

from defect.models import (
    Location, 
    Type, 
    Position, 
    LocationType, 
    TypePosition,
)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('nID', 'sName', 'sDescription', 'nParentID')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('nID', 'sName', 'sDescription', 'nParentID')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('nID', 'sName', 'sDescription', 'nParentID')

class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('nLocationID', 'nTypeID', 'nHidden', 'dtCreated_at', 'dtUpdatedAt')

class TypePositionAdmin(admin.ModelAdmin):
    list_display = ('nTypeID', 'nPositionID', 'nHidden', 'dtCreated_at', 'dtUpdatedAt')
    
admin.site.register(Location, LocationAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
admin.site.register(TypePosition, TypePositionAdmin)

