from django.shortcuts import render
from . models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')
def contact(request):
    if request.method == "POST":
        fullName=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        try:
            contact=Contact.objects.create(fullName=fullName,email=email,subject=subject,message=message)
            messages.info(request,'Message sent Successfully, I will contact you through the email you provided !')

        except:
            messages.info(request,'Something went wrong , please try again ')

    return render(request,'index.html')





