from django import forms
from core_app.models import core_object

class core_object_form(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    width = forms.IntegerField(label='Width')
    height = forms.IntegerField(label='Height')
    weight = forms.IntegerField(label='Weight')

class edit_core_object_form(forms.ModelForm):

    class Meta:
        model = core_object
        fields = ['name', 'width', 'height', 'weight']