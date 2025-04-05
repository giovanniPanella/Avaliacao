
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/agegroups/', include('agegroups.urls')),
    path('api/', include('users.urls')),
]
