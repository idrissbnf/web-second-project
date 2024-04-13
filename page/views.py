from django.shortcuts import render


# Create your views here.
def index (request) :
    return render(request,'index.html')
def style (request):
    return render (request,'styles.css')