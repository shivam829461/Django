from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    dict={
        "title":"Landing Page","body":"Smile!!!!!!!!",
        "list":[1,2,"Call",4,5],
        "nums":[1,2,45,4,5,],
        "dictionary":[{"name":"Shivam","phone":123456789},{"name":"Ujjwal","phone":172914}]
    }
    return render(request,"index.html",dict)

def hello(request):
    return HttpResponse("<p><b>Hello \n"*100)

def dynamic(request,dy):
    return HttpResponse(dy)
