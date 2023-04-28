from django.shortcuts import render

# Create your views here.
def student(request):
    return render(request,'enroll/home.html')
def detail(request,my_id=1):
    st={'id':my_id}
    return render(request,'enroll/student.html',st)

def subdetail(request,my_id,my_subid):
    if my_id==1 and my_subid==5:
        st={'id':my_id,'name':'rehan Allah wala','info':'sub details'}
    if my_id==2 and my_subid==6:
        st={'id':my_id,'name':'Azad Chaiwala','info':'sub details'}
    if my_id==3 and my_subid==7:
        st={'id':my_id,'name':'Farhan Mirchwala','info':'sub details'}
    return render(request,'enroll/student.html',st)