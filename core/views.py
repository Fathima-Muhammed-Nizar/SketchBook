

# Create your views here.
from django.shortcuts import render, redirect

from item.models import Category, Item
from django.contrib.auth.models import User

from .forms import SignupForm

def index(request):
    artists = User.objects.all()
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'artists': artists
    })

def exibition(request, id):
    artist = User.objects.get(id=id)
    items = Item.objects.filter(created_by=artist)

    return render(request, 'core/exibition.html', {
        'items': items,
        'user': artist,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
