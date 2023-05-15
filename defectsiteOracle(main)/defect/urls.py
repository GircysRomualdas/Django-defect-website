from django.urls import path

from .views import *

app_name = 'defect'

urlpatterns = [
    path('location/', allLocationsView, name='allLocationsView'),
    path('location/create', createLocationView, name="createLocationView"),
    path('location/<int:id>', updateLocationView, name='updateLocationView'),
    path('location/delete/<int:id>', deleteLocationView, name='deleteLocationView'),
    path('location/search', searchLocationView, name='searchLocationView'),

    path('type/', allTypesView, name='allTypesView'),
    path('type/create', createTypeView, name="createTypeView"),
    path('type/<int:id>', updateTypeView, name='updateTypeView'),
    path('type/delete/<int:id>', deleteTypeView, name='deleteTypeView'),
    path('type/search', searchTypeView, name='searchTypeView'),

    path('position/', allPositionsView, name='allPositionsView'),
    path('position/create', createPositionView, name="createPositionView"),
    path('position/<int:id>', updatePositionView, name='updatePositionView'),
    path('position/delete/<int:id>', deletePositionView, name='deletePositionView'),
    path('position/search', searchPositionView, name='searchPositionView'),

    path('custom/', customView, name='customView'),
    path('custom2/', custom2View, name='custom2View'),
]