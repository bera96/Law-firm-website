from employee.models import Employee,PracticeAreas



def header_data(request):

    context_practice_areas = PracticeAreas.objects.all()
    context_employees = Employee.objects.all()

    context = {
        'context_practice_areas':context_practice_areas,
        'context_employees':context_employees,

    }
    return context

