from django.shortcuts import get_object_or_404, render
from .models import Yoga,Trainer
from django.views import generic
from django.http import request

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def classes(request):
    return render(request,'classes.html')

def events(request):
    return render(request,'events.html')

class YogaListView(generic.ListView):
    model = Yoga

class YogaDetailView(generic.DetailView):
    model = Yoga
    def yoga_detail_view(self,primary_key):
        yoga = get_object_or_404(Yoga,pk = primary_key)
        return render(request , 'yoga/yoga_detail.html' , context={'yoga':yoga})