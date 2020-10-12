from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),    
    path('sports/',include('sports.urls')),
    # path('fitness/',include('fitness.urls')),
]
