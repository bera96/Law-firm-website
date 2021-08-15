from employee.models import Employee,PracticeAreas
from main.models import GeneralSettings



def header_data(request):

    context_practice_areas = PracticeAreas.objects.all()
    context_employees = Employee.objects.all()

    context = {
        'context_practice_areas':context_practice_areas,
        'context_employees':context_employees,

    }
    return context


def general_data(request):

    settings = GeneralSettings.objects.all()
    

    context = {
        'settings':settings,

    }
    return context

