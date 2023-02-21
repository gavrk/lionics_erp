from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # /admin/
    path('admin/', admin.site.urls),

    # /docs/~
    path('docs/', include('docs.urls')),

    # /companies/
    path('companies/', include('companies.urls')),
]
