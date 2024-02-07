from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'index.html')
def menu(request):
    return render(request, 'menu.html')
def franchise(request):
    return render(request, 'franchise.html')

