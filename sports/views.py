from django.shortcuts import render
from .models import Academy,Sports,Coach
# Create your views here.
 

def index(request):
    acd = Academy.objects.all()
    ch = Coach.objects.all()

    # print(acd[0].name,ch[0].name)
    return render(request,'sports/index.html',context={'dic1':acd,'dic2':ch})