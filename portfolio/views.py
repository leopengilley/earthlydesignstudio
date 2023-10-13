from django.shortcuts import render
from .models import BlogPost, Gallery, BlogImage
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from .forms import ContactForm

def home(request):
    events = BlogPost.objects.all().order_by('date', 'id')
    paginator = Paginator(events, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj, 'paginator': paginator})

def about_me(request):
    return render(request, 'about_me.html')

def contact(request):

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]

            recipients = ["veronqiue.sellies@gmail.com"]

            try:
                send_mail(subject, message, sender, recipients)

            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            return HttpResponseRedirect("/contact/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def gallery(request):
    gallery = Gallery.objects.all()

    return render(request, 'gallery.html', {'gallery': gallery})
