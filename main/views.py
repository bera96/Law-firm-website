from django.shortcuts import redirect, render,get_object_or_404
from .forms import MessageForm
from .models import Faqs
from django.contrib import messages
from employee.models import Employee, PracticeAreas



def home_view(request):

    return render(request, 'main/home.html', {})





def contact_view(request):

    if request.method == "POST":
        
        contact_form = MessageForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request,'Mesajınız alınmıştır.')
            return redirect('main:home')
    else:
        contact_form = MessageForm()

    context = {
        'form':contact_form
    }



    return render(request, 'main/contactus.html',context ) 





def questions_view(request):

    faqs = Faqs.objects.all()
    faqs_even = [faq for faq in faqs if faq.id%2==0]
    faqs_odd = [faq for faq in faqs if not faq.id%2==0]

    context = {
        'faqs_odd':faqs_odd,
        'faqs_even':faqs_even,
    }

    return render(request, 'main/faqs.html',context ) 







def aboutus_view(request):

    employees = Employee.objects.all()
    context = {
        'employees':employees,
    }
    return render(request, 'main/aboutus.html',context)



    

def practice_areas_view(request,slug):

   
    current_area = get_object_or_404(PracticeAreas,slug=slug)
    practice_areas = PracticeAreas.objects.all()
    context = {
        'practice_areas':practice_areas,
        'current_area':current_area,
    }

    return render(request, 'main/practiceareas.html', context ) 
