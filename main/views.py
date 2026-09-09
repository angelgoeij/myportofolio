from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Goeij Angelatika Goeyanto",
        "npm": "2506656772",
        "study_program": "Sistem Informasi",
        "bio": (
            "── ⟡ ๋࣭ ࣪ Information System Student at the Faculty of Computer Science in Universitas Indonesia. Interested in the intersection of technology and socio-scientific problems, and how information systems can create meaningful solutions."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Goeij Angelatika Goeyanto",
        "experience_list": Experience.objects.all(),
        
    }
    
    return render(request, "experience.html", context)

