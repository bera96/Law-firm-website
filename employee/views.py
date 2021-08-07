from django.shortcuts import get_object_or_404, render
from .models import Employee


#All employees is send by the about_view inside main app .


def employee_detail(request,slug):
    
    employees = Employee.objects.all()
    employee = get_object_or_404(Employee,slug=slug)
    
    context = {
        'employee':employee,
        'employees':employees,
    }
    return render(request, 'employee/detail.html',context)
