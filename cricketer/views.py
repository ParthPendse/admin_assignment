
from django.shortcuts import render


# Create your views here.
from cricketer.models import Cricketer


def index(request):
    cricketer_list= Cricketer.objects.all()
    return render(request,'index.html',{'cricketer':cricketer_list})
