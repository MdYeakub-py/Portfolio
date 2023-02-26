from django.shortcuts import render, redirect
from .models import InfoDetails, Education, Services, Protfolio, AdminContact
from .forms import AdminContactForm
# for SEndig email and contact


from django.core.mail import send_mail
from django.contrib.messages import constants as messages
# Create your views here.


def index(request):
    return render(request, 'index.html',)


def index(request):

    # for informations section
    informations = InfoDetails.objects.all()

    # for Education section
    educations = Education.objects.all()

    # for Services Section

    services = Services.objects.all()

    # for Protfolio or Project
    images = Protfolio.objects.all()

    # for contact form
    if request.method == 'POST':
        form = AdminContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject =form.changed_data['subject']
            message = form.cleaned_data['message']
            
            # Save the form data to the database
            AdminContact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            # Send an email
            send_mail(
                'Subject here',
                'Here is the message.',
                'email',
                ['md.yeakub47@gmail.com'],
                fail_silently=False,
            )
            
            return redirect('contact_success')
    else:
        form = AdminContactForm()
    return render(request, 'index.html', {'informations': informations, 'educations': educations, 'services': services, 'images': images,'form': form })


