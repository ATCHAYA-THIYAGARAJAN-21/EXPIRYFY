from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


from django import forms
from .models import Rack

class RackForm(forms.ModelForm):
    class Meta:
        model = Rack
        fields = ['rack_no', 'product_name', 'product_image']

