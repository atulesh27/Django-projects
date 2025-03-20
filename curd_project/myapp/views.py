from django.shortcuts import render, redirect
from .models import EmployeeData
from .form import EmployeeForm

# Create your views here.

# Create (Insert) and Read (Retrieve)

def employee_list(request):
    employees = EmployeeData.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_list.html', {'employees': employees, 'form': form})

# update

def employee_update(request, id):
    employee = EmployeeData.objects.get(id =id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_update.html', {'form': form})

# Delete
def employee_delete(request, id):
    employee = EmployeeData.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')

