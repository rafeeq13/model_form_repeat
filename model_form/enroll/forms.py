from django import forms
from .models import User
class Student(forms.ModelForm):
    name=forms.CharField(max_length=30,error_messages={'required':"re enter your name"})
    class Meta:
        model=User
        fields=['name','email','address']
        labels={'name':'enter Name','email':'enter email',
                'address':'enter address'}
        widgets={'email':forms.TextInput(attrs={'placeholder':'enter your name here'})}
        
        
    


          