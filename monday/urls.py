from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('landing.urls','monday'), namespace='landing')),
    
]
urlpatterns += staticfiles_urlpatterns()