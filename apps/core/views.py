from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from .models import CatPost


# Two example views. Change or delete as necessary.

class NewCatPost(forms.Form):
    catname = forms.CharField(max_length=120)
    neighborhood = forms.CharField(max_length=120)
    text = forms.CharField()
    image = forms.URLField(max_length=120)
    sighted = forms.DateTimeField()
#widget=forms.SelectDateWidget
# widget=forms.Textarea

def home(request):

    context = {
        'example_context_variable': '9 out of 10 cats approve',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


def view_cats(request):
    all_cats = CatPost.objects.all()
    if not request.user.is_authenticated:
        messages.warning(request, "You need to log in to view the cats.")
        return redirect('/')
    
    else:
        form = NewCatPost()

    context = {
        'all_cats': all_cats,
        'form': form,
    }

    return render(request, 'pages/cats.html', context)

def add_a_cat(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to log in to add a cat.")
        return redirect('/')
    if request.method == 'POST':
        form = NewCatPost(request.POST)
        if form.is_valid():
            CatPost.objects.create(**form.cleaned_data)
            messages.warning(request, "Thanks for registering your feline friend!")
            return redirect('/')

    else:
        form = NewCatPost()

    context = {
        'form': form,
    }

    return render(request, 'pages/cats.html', context)

