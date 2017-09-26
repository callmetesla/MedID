from django.shortcuts import render,HttpResponse
#Home page view
def home(request):
    return render(request,'medid/home.html')
