from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "shade", "size"]

    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

   
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)

   
    def clean_shade(self):
        shade = self.cleaned_data["shade"]
        return strip_tags(shade)

    
    def clean_size(self):
        size = self.cleaned_data["size"]
        return strip_tags(size)