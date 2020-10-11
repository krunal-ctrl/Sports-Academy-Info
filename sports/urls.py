from django.urls import path
from . import views
from django.views.generic import RedirectView
urlpatterns = [
    # path('',views.index , name='sportsindex'),
    path('', RedirectView.as_view(url='/list/', permanent=True)),
    path('list/',views.AcademyListView.as_view() , name = 'academy-list')
]
# /sports/list/






