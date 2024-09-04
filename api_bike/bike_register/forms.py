from django import forms
from .models import Bike

class pagina_form(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'

class index_form(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['nome']

class index_form_put(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'