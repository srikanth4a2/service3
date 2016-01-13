from django.shortcuts import render

from django.http import HttpResponseRedirect,HttpResponse

from django.core.mail import send_mail, EmailMessage

from .forms import ContactForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
    	    sender = form.cleaned_data['sender']
    	    cc_myself = form.cleaned_data['cc_myself']
    	    files = request.FILES['files']

            recipients = ['s.duddugunta@direction.biz']
    	    if cc_myself:
        	    recipients.append(sender)

    	    mail=EmailMessage(subject, message, sender, recipients)
    	    mail.attach(files.name, files.read(), files.content_type)
    	    mail.send()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'name.html', {'form': form})

def thanks(request):
	return HttpResponse('Thankyou,successfully sent the mail')