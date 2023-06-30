from django.shortcuts import render
from django.core.mail import send_mail
from mywebsite import settings
from django.contrib import messages



# def index(request):
#     return render(request,'index.html')


def index(request):

    print(request.POST)

    if request.method=="POST":
        subject= request.POST["name"] +"-" + request.POST["email"] + "-" + request.POST["number"]
        message=request.POST["topic"] + " " + request.POST["message"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["andrealejandrog@gmail.com"]

        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        messages.success(request, '¡La información ha sido enviada correctamente!')
        
        return render(request,'index.html')
    else:
    
        return render(request,'index.html')
        
