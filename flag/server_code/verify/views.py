from django.shortcuts import render
from django.http import HttpResponse
from .models import Flag
import ipware

# Create your views here.

def start(request):
    print('started')
    return HttpResponse("submit your flags here. <br> <form action='/add'><input type='text' name='val'/><input type='submit'></form> ")

def add(request):
    ip = ipware.get_client_ip(request)[0]
    #ip = request.
    val = request.GET['val']
    if val in []:
        valid = True
    else:
        valid = False
    f = Flag(ip_addr = ip, flag = val, valid=valid)
    f.save()
    return HttpResponse(f'successfully added {ip} with flag {val}')

