from django.shortcuts import render
from django.http import HttpResponse
from .models import Flag

# Create your views here.

def start(request):
    print('started')
    return HttpResponse("server is running. <br> To login and see <a href='admin/'> click here </a>")

def add(request):
    ip = request.GET['ip']
    val = request.GET['val']
    f = Flag(ip_addr = ip, flag = val)
    f.save()
    return HttpResponse(f'successfully added {ip} with flag {val}')

