from django import forms
from .models import Product, Category
from pyuploadcare.dj.forms import ImageField, FileWidget

class ProductForm(forms.ModelForm):
    image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
    class Meta:
        model=Product
        fields=('name', 'price', 'stock', 'Category', 'image')