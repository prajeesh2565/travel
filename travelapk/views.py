from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):
    obj = place.objects.all()
    obj2=team.objects.all()
    return render(request,'index.html', {'object': obj,'members':obj2})