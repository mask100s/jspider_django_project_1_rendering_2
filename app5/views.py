from django.shortcuts import render

# Create your views here.

def htmlpage1(request):
  return render(request,'htmlpage1.html')

def htmlpage2(request):
  return render(request,'htmlpage2.html')

def htmlpage3(request):
  return render(request,'htmlpage3.html')

def htmlpage4(request):
  return render(request,'htmlpage4.html')