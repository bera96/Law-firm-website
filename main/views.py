from django.shortcuts import redirect, render
from .forms import MessageForm
from django.contrib import messages



def home_view(request):

    return render(request, 'main/home.html', {})





def contact_view(request):

    if request.method == "POST":
        contact_form = MessageForm(request.POST)
        print(request.POST)
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

