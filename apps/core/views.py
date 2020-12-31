from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from .models import CatPost


# Two example views. Change or delete as necessary.

class NewCatPost(forms.Form):
    catname = forms.CharField(max_length=120)
    neighborhood = forms.CharField(max_length=120)
    text = forms.CharField()
    image = forms.URLField()
    sighted = forms.DateTimeField()

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
    form = NewCatPost()
    if not request.user.is_authenticated:
        messages.warning(request, "You need to log in to view the cats.")

    context = {
        'all_cats': all_cats,
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

    return render(request, 'pages/add_a_cat.html', context)

def view_cat_bio(request, cat_id):
	catpost = CatPost.objects.get(id=cat_id)
	print("Cat bio requested " + cat_id)

	name = catpost.catname
	hood = catpost.neighborhood
	text = catpost.text
	image = catpost.image
	sighted = catpost.sighted
	cat_id = catpost.id
	print("cat name = " + name)

	context = {
	    'name': name,
	    'hood': hood,
	    'text': text,
	    'image': image,
	    'sighted': sighted,
	    'cat_id': cat_id
	}
	return render(request, "pages/single_cat_post.html", context)
