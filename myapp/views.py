from unicodedata import category
from django.shortcuts import render
from .models import Award, Service, Categories
from django.core.mail import send_mail

# Create your views here.
def Home(request):
    clover = Award.objects.filter(category='1').order_by('-Year')[:4]
    others = Award.objects.filter(category='2').order_by('-Year')[:4]
    services = Service.objects.all().order_by('title')[:2]
    

    context = {
        'services': services,
        'clover':clover,
        'others': others,
        
    }

    return render(request, 'index.html',context)
def Award_cert(request):
    awards = Award.objects.all().order_by('-Year')
    clover = Award.objects.filter(category='1').order_by('-Year')
    others = Award.objects.filter(category='2').order_by('-Year')
    cat = Categories.objects.filter(name='Clover Mama Afrika')

    context = {
        'awards': awards,
        'clover':clover,
        'others': others,
        'cat': Categories
    }

    return render(request, 'awards.html',context)
def Service_re(request):
    services = Service.objects.all().order_by('-title')
    

    context = {
        'services': services
    }

    return render(request, 'services.html',context)

def contact(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
    
        data = {
            'name':name,
            'email': email,
            'subject': subject,
            'message':message,
        }
        email = f'''
        message : {data['message']}

        from : {data['email']}

        '''
        send_mail(data['subject'], email, '', ['miguelmehgoss@gmail.com'])

    

    return render(request, 'contact.html')