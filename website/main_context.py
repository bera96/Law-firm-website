from employee.models import Employee,PracticeAreas
from main.models import GeneralSettings



def general_data(request):

    context_practice_areas = PracticeAreas.objects.all()
    context_employees = Employee.objects.all()
    settings = GeneralSettings.objects.all()

    context = {
        'context_practice_areas':context_practice_areas,
        'context_employees':context_employees,
        'context_settings':settings,

    }
    return context


