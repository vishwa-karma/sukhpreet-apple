
from django.contrib import admin
from django.urls import path ,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cstats.urls')),
    path('accounts/', include('accounts.urls')),
]
