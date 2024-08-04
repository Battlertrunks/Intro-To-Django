# from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
  # return HttpResponse('Hello World! I am here.')
  return render(request, 'home.html')

def aboutPage(request):
  #return HttpResponse('This is the about page.')
  return render(request, 'aboutPage.html')