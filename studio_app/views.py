from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'login.html')  

def signup(request):
    return render(request,'register.html')  

def about(request):
    return render(request,'about.html')  

def contact(request):
    return render(request,'contact.html')  

def services(request):
    return render(request,'services.html') 

def joinus(request):
    return render(request,'joinus.html') 

def booking(request):
    return render(request,'booking.html')                         

def gallery(request):
    return render(request,'gallery.html')           
