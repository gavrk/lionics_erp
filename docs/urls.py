from django.urls import path
from . import views

app_name = "docs"

urlpatterns = [
    # /docs/
    path('index/', views.index, name='index'),

    # /docs/standard_tes/
    path('register_stc/', views.StandardTesCreate.as_view(), name='register_stc'),

]