from django.urls import path

from .views import *

app_name = 'defect'

urlpatterns = [
    path('location/', allLocationsView, name='allLocationsView'),
    path('location/create/', createLocationView, name="createLocationView"),
    path('location/<int:id>/', updateLocationView, name='updateLocationView'),
    path('location/delete/<int:id>/', deleteLocationView, name='deleteLocationView'),
    path('location/search/', searchLocationView, name='searchLocationView'),
    
    path('location/assign/<int:id>/type/', assignLocationTypeView, name='assignLocationTypeView'),
    path('location/assign/<int:id>/type/search/', searchAssignLocationTypeView, name='searchAssignLocationTypeView'),
    path('location/assign/<int:lid>/type/add/<int:tid>', addLocationTypeView, name='addLocationTypeView'),
    path('location/assign/<int:lid>/type/remove/<int:tid>', removeLocationTypeView, name='removeLocationTypeView'),

    path('location/assign/<int:id>/parent/', assignLocationParentView, name='assignLocationParentView'),
    path('location/assign/<int:id>/parent/search/', searchAssignLocationParentView, name='searchAssignLocationParentView'),
    path('location/assign/<int:lid>/parent/add/<int:parentid>', addLocationParentView, name='addLocationParentView'),
    path('location/assign/<int:lid>/parent/remove/', removeLocationParentView, name='removeLocationParentView'),
    

    path('type/', allTypesView, name='allTypesView'),
    path('type/create/', createTypeView, name="createTypeView"),
    path('type/<int:id>/', updateTypeView, name='updateTypeView'),
    path('type/delete/<int:id>/', deleteTypeView, name='deleteTypeView'),
    path('type/search/', searchTypeView, name='searchTypeView'),

    path('type/assign/<int:id>/position/', assignTypePositionView, name='assignTypePositionView'),
    path('type/assign/<int:id>/position/search/', searchAssignTypePositionView, name='searchAssignTypePositionView'),
    path('type/assign/<int:tid>/position/add/<int:pid>', addTypePositionView, name='addTypePositionView'),
    path('type/assign/<int:tid>/position/remove/<int:pid>', removeTypePositionView, name='removeTypePositionView'),

    path('type/assign/<int:id>/parent/', assignTypeParentView, name='assignTypeParentView'),
    path('type/assign/<int:id>/parent/search/', searchAssignTypeParentView, name='searchAssignTypeParentView'),
    path('type/assign/<int:tid>/parent/add/<int:parentid>', addTypeParentView, name='addTypeParentView'),
    path('type/assign/<int:tid>/parent/remove/', removeTypeParentView, name='removeTypeParentView'),


    path('position/', allPositionsView, name='allPositionsView'),
    path('position/create/', createPositionView, name="createPositionView"),
    path('position/<int:id>/', updatePositionView, name='updatePositionView'),
    path('position/delete/<int:id>/', deletePositionView, name='deletePositionView'),
    path('position/search/', searchPositionView, name='searchPositionView'),

    path('position/assign/<int:id>/parent/', assignPositionParentView, name='assignPositionParentView'),
    path('position/assign/<int:id>/parent/search/', searchAssignPositionParentView, name='searchAssignPositionParentView'),
    path('position/assign/<int:pid>/parent/add/<int:parentid>', addPositionParentView, name='addPositionParentView'),
    path('position/assign/<int:pid>/parent/remove/', removePositionParentView, name='removePositionParentView'),

]