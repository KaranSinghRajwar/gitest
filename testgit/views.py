from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def testgit(request):
    return HttpResponse('<b>This is the homepage<b>')