from django import forms

from .models import Location, Type, Position, LocationType

class LocationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(LocationForm, self).__init__(*args, **kwargs)
       nParentID = forms.ModelChoiceField(queryset=Location.objects.all().exclude(nID=self.instance.nID),  widget=forms.Select, required=False)
       self.fields['nParentID'] = nParentID

    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Location
        fields = ('__all__')
        

class TypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(TypeForm, self).__init__(*args, **kwargs)
       nParentID = forms.ModelChoiceField(queryset=Type.objects.all().exclude(nID=self.instance.nID),  widget=forms.Select, required=False)
       self.fields['nParentID'] = nParentID

    position = forms.ModelMultipleChoiceField(queryset=Position.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Type
        fields = ('__all__')

class PositionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(PositionForm, self).__init__(*args, **kwargs)
       nParentID = forms.ModelChoiceField(queryset=Position.objects.all().exclude(nID=self.instance.nID),  widget=forms.Select, required=False)
       self.fields['nParentID'] = nParentID

    class Meta:
        model = Position
        fields = ('__all__')



# temp 
class LocationTypeForm(forms.ModelForm):

    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Location
        fields = ('__all__')

