from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [ 
    path('yoga/',views.YogaListView.as_view() , name = 'yoga'),
    path('center/<int:pk>', views.YogaDetailView.as_view(), name='yoga-detail'),
]