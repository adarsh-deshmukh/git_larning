from socket import fromshare
from django import forms
from .models import employee,Position
class employeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields="__all__"
        labels={
            'fullname':'FUll Name',
            'emp_code':'Emp. Code'
        }
    
    def __init__(self,*args,**kwargs):
        super(employeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="select"
        self.fields['emp_code'].required=False

