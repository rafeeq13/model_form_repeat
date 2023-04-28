from django.shortcuts import render

# Create your views here.
def details(request,year):
    return render (request,'enroll/custom.html',{'yyyy':year})