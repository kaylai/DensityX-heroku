from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('SiO2', 'TiO2', 'Al2O3', 'Fe2O3', 'FeO', 'CaO', 'MgO', 'Na2O', 'K2O', 'H2O', 'P', 'T',)