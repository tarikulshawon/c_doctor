from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):

    return render(request, 'cDoc/homePage.html')

def a(request):
    return render(request, 'cDoc/a.html')
def b(request):
    return render(request, 'cDoc/b.html')