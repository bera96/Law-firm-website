from django.shortcuts import get_object_or_404, render
from .models import Employee







def employee_detail(request,slug):

    employee = get_object_or_404(Employee,slug=slug)

    context = {
        'employee':employee
    }
    return render(request, 'employee/detail.html',context)
