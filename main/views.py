# Create your views here.
from django.shortcuts import render

from main.models import Education, Experience, Project

from main.forms import ContactForm, EducationForm, ProjectForm

from django.core.mail import send_mail

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Goeij Angelatika Goeyanto",
        "project_list": Project.objects.all(),

    }

    return render(request, "projects.html", context)

def show_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"Portfolio message from {name}",
                message=f"Email: {email}\n\n{message}",
                from_email="your-email@gmail.com",
                recipient_list=["your-email@gmail.com"],
            )
            
            return render(request, "contact.html", {
                "form": ContactForm(),
                "success": True,
            })
    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form,
    })


def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Goeij Angelatika Goeyanto",
        "form": form,
    }
    return render(request, "projects_form.html", context)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def show_education(request):
    json_response = get_education_json(request)

    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education = [education.object for education in education]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Goeij Angelatika Goeyanto",
        "education_list": Education.objects.all(),

    }

    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Goeij Angelatika Goeyanto",
        "form": form,
    }
    return render(request, "education_form.html", context)


def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    education = Education.objects.all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    education = Education.objects.all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")
