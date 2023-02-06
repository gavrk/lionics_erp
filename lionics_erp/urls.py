from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # /admin/
    path('admin/', admin.site.urls),

    # /doc_generator/~
    path('doc_generator/', include('doc_generator.urls')),

    # /companies/
    path('companies/', include('companies.urls')),
]
