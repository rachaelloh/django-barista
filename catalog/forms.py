from django import forms
from .models import Product, Category
from pyuploadcare.dj.forms import ImageField, FileWidget

class ProductForm(forms.ModelForm):
    image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
    class Meta:
        model=Product
        fields=('name', 'description', 'price', 'Category', 'image')
        
class ProductSearchForm(forms.Form):
    search_terms = forms.CharField(required=False)
    min_cost = forms.FloatField(required=False, min_value=0)
    max_cost = forms.FloatField(required=False)
