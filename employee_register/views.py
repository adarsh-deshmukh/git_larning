from django.shortcuts import render,redirect
from .forms import employeeForm
from.models import employee
# Create your views here.
def employee_list(request):
    a=employee.objects.all()
    return render(request,"employee_list.html",{"a":a})

def employee_form(request):
    form = employeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("emplist")
    return render(request,"employee_form.html",{"form":form})

def employee_update(request,x):
    form = employeeForm()
    a=employee.objects.get(id=x)
    if request.method == "GET":
        form = employeeForm(request.POST or None,instance=a)
        if form.is_valid():
            form.save()
            return redirect("emplist")
    return render(request,"employee_update.html",{"form":form})


#def employee_delete(request):
    #return render(request)
