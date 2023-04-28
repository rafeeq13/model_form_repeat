from django.shortcuts import render
from .forms import Student
from .models import User
# Create your views here.
def sudden(request):
    return render(request,'enroll/success.html')
def details(request):
    if request.method=='POST':
        pi=User.objects.get(pk=1)
        st=Student(request.POST ,instance=pi)
        if st.is_valid():
            st.save()
    else:
        st=Student()
    return render(request,'enroll/student.html',{'form':st})