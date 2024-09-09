from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Dhania Tiaraputri Herdiani',
        'class' : 'PBP B',
        'npm' : '2306165881',
        'product' : 'Peptide Lip Tint',
        'description': 'A nourishing  and tinted lip product that gives you the perfect gloss on your lips. The fragrance-free formula leaves lips feeling hydrated and visibly plump.',
        'shade' : 'Ribbon pink',
        'size' : '10 ml',
        'price': '380000'
    }

    return render(request, "main.html", context)