from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),    
    path('',views.about,name='about'), 
    path('sports/',include('sports.urls')),
    path('fitness/',include('fitness.urls')),
    path('yoga/',include('yoga.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)