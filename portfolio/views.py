from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *

from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()

        context['projects'] = FeaturedProject.objects.all()
        
        return context
    

# ================ CONTACT =================
def index(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data['sender_name']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            
            html = render_to_string('emails/contactform.html', {
                'sender_name' : sender_name,
                'from_email' : from_email,
                'message' : message,
            })

            send_mail("subject", "message", "from_email", ["afcportfolio@gmail.com"], html_message=html)

            return redirect('/contact')
        
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {
        'form' : form
    })