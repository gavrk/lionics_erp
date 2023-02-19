from django.urls import path
from . import views

app_name = "companies"


urlpatterns = [
    # /companies/index_loc
    path('index_loc/', views.index_loc, name='index_loc'),

    # /companies/index_int
    path('index_int/', views.index_int, name='index_int'),

    # /companies/register_loc/some_new_companyloc_id
    path(r'register_loc/', views.CompanyLocCreate.as_view(), name='register_loc'),

    # /companies/index_loc/some_id/delete_loc
    path(r'index_loc/<int:pk>/delete_loc/', views.CompanyLocDelete.as_view(), name='delete_loc'),

    # /companies/index_loc/some_id/
    path('index_loc/<int:pk>/', views.CompanyLocUpdate.as_view(), name='detail_loc'),

    # /companies/register_int/
    path('register_int/', views.register_int, name='register_int'),

    # /companies/detail_int/some_id/
    path('index_int/<int:companyint_id>/', views.detail_int, name='detail_int'),
]