from django.contrib import admin
from django.urls import path, include

from shortenerapp.views import root


urlpatterns = [
    path('', include('shortenerapp.urls')),
    path('admin/', admin.site.urls),
    path('<str:url_hash>/', root, name='root'),

]
