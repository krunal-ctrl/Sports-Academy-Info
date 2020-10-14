from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [    
    path('academy/',views.AcademyListView.as_view() , name = 'academy'),
    path('academy/<int:pk>', views.AcademyDetailView.as_view(), name='academy-detail'),
]