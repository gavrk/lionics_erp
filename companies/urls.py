from django.urls import path
from . import views


urlpatterns = [
    # /companies/
    path('', views.index, name='index'),

    # /companies/register_loc/some_new_companyloc_id
    path(r'register_loc/$', views.CompanyLocCreate.as_view(), name='register_loc'),

    # /companies/detail_loc/some_id/
    path('detail_loc/<int:companyloc_id>/', views.detail_loc, name='detail_loc'),

    # /companies/register_int/
    path('register_int/', views.register_int, name='register_int'),

    # /companies/detail_int/some_id/
    path('detail_int/<int:companyint_id>/', views.detail_int, name='detail_int'),

    # /companies/type_selected/
    path('type_selected/', views.type_selected, name='type_selected'),
]