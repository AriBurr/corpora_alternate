from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.languages.urls')),
    path('', include('apps.uploads.urls')),
    path('', include('apps.recommenders.urls')),    
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
