from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    a = 10
    b = 5
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    # return HttpResponse("Hello Human!")
    return render(request,'hello_world.html',locals())

def add(request, a, b):
    s = a + b
    return HttpResponse(s)