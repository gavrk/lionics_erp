from django.urls import path
from . import views


urlpatterns = [
    # /companies/
    path('', views.index, name='index'),

    # /companies/register_loc/
    path('register_loc/', views.register_loc, name='register_loc'),

    # /companies/edit_or_delete_loc/
    path('edit_or_delete_loc/', views.edit_or_delete_loc, name='edit_or_delete_loc'),

    # /companies/register_int/
    path('register_int/', views.register_int, name='register_int'),

    # /companies/edit_or_delete_int/
    path('edit_or_delete_int/', views.edit_or_delete_int, name='edit_or_delete_int'),
]