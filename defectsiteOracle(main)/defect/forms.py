from django import forms
from django.db.models import Q

from .models import *

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('__all__')
        exclude = ["nParentID", "type"]

class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ('__all__')
        exclude = ["nParentID", "position"]

class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ('__all__')
        exclude = ["nParentID"]


