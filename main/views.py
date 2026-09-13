# Create your views here.
from django.shortcuts import render

from main.models import Experience, Project

from main.forms import ContactForm


def show_main(request):
    form = ContactForm()
    context = {
        "name": "Goeij Angelatika Goeyanto",
        "npm": "2506656772",
        "study_program": "Sistem Informasi",
        "bio": (
            "── ⟡ ๋࣭ ࣪ Information System Student at the Faculty of Computer Science in Universitas Indonesia. Interested in the intersection of technology and socio-scientific problems, and how information systems can create meaningful solutions."
        ),
        "form": form,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Goeij Angelatika Goeyanto",
        "experience_list": Experience.objects.all(),
        
    }
    
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Goeij Angelatika Goeyanto",
        "project_list": Project.objects.all(),

    }

    return render(request, "projects.html", context)

def show_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            return render(request, "contact.html", {
                "form": ContactForm(),
                "success": True,
            })
    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form,
    })
