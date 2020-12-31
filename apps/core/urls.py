from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.view_cats, name='cats'),
    path('add-cat/', views.add_a_cat, name='addcat'),
    path('cat/<cat_id>/', views.view_cat_bio, name='catbio'),
]
