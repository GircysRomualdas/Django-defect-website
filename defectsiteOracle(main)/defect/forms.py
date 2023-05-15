from django import forms

from .models import Location, Type, Position, LocationType

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('sName', 'sDescription')

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ('sName', 'sDescription')

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('sName', 'sDescription')

class LocationTypeForm(forms.Form):
    class Meta:
        model = LocationType
        fields = '__all__'

