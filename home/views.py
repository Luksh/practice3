from django.shortcuts import render
from home.models import Contact, Feedback

# Create your views here.

def home(request):
    review = {}
    review['comment'] = Feedback.objects.all()
    return render(request,'index.html',review)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        message = {'success':'The form is submitted'}

        return render(request,'contact.html',message)

    return render(request,'contact.html')











