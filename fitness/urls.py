from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    #path('',views.index , name='sportsindex'),
    path('fitness/',views.FitnessListView.as_view() , name = 'fitness'),
    path('fitness/<int:pk>', views.FitnessDetailView.as_view(), name='fitness-detail'),
]
