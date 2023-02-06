from django.urls import path
from . import views


urlpatterns = [
    # /doc_generator/
    path('', views.index, name='index'),

    # /doc_generator/standard_tes/
    path('standard_tes/', views.standard_tes, name='standard_tes'),

    # /doc_generator/standard_customs/
    path('standard_customs/', views.standard_customs, name='standard_customs'),
]