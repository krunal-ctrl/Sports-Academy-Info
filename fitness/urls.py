from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [    
    path('fitness/',views.FitnessListView.as_view() , name = 'fitness'),
    path('club/<int:pk>', views.FitnessDetailView.as_view(), name='fitness-detail'),
]