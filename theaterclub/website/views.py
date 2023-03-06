from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def application(request):
  return render(request, 'application.html')