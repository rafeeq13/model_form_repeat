from django.shortcuts import render

# Create your views here.
def detail(request):
    return render(request,'enroll/student.html')

def student(request,my_id):
    stu={'id':my_id,'name':'ali'}
    print(stu)
    return render(request,'enroll/home.html',stu)

def subdetail(request,my_id,my_subid):
    if my_id==1 and my_subid==4:
        student={'id':my_id,'name':'rafeeq','info':'unavailable'}
    if my_id==2 and my_subid==5:
        student={'id':my_id,'name':'rafeeq','info':'unavailable'}
    if my_id==6 and my_subid==7:
        student={'id':my_id,'name':'rafeeq','info':'unavailable'}
    return render(request,'enroll/home.html')
