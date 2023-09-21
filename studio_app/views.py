from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'login.html')  

def signup(request):
    return render(request,'register.html')       
