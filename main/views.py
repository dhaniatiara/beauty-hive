from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'name' : 'Peptide Lip Tint',
        'price': '380000',
        'description': 'A nourishing  and tinted lip product that gives you the perfect gloss on your lips. The fragrance-free formula leaves lips feeling hydrated and visibly plump.',
        'shade' : 'Ribbon pink',
        'size' : '10 ml',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)