from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def boking(request):
    return render(request,'booking.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,"testimonial.html")

def contract(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')