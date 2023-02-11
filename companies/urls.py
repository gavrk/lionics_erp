from django.urls import path
from . import views


urlpatterns = [
    # /companies/index_loc
    path('index_loc/', views.index_loc, name='index_loc'),

    # /companies/index_int
    path('index_int/', views.index_int, name='index_int'),

    # /companies/register_loc/some_new_companyloc_id
    path(r'register_loc/', views.CompanyLocCreate.as_view(), name='register_loc'),

    # /companies/detail_loc/some_id/
    path('detail_loc/<int:companyloc_id>/', views.detail_loc, name='detail_loc'),

    # /companies/register_int/
    path('register_int/', views.register_int, name='register_int'),

    # /companies/detail_int/some_id/
    path('detail_int/<int:companyint_id>/', views.detail_int, name='detail_int'),
]