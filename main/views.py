# Create your views here.
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        

from main.models import Education, Experience, Project
from main.forms import ContactForm, EducationForm, ProjectForm

from django.core.mail import send_mail

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import datetime

from django.views.decorators.http import require_POST

def show_main(request):
    form = ContactForm()
    last_login = request.COOKIES.get('last_login','No active login session/Cookie not found')
    context = {
        "name": "Goeij Angelatika Goeyanto",
        "npm": "2506656772",
        "study_program": "Sistem Informasi",
        "bio": (
            "── ⟡ ๋࣭ ࣪ Information System Student at the Faculty of Computer Science in Universitas Indonesia. Interested in the intersection of technology and socio-scientific problems, and how information systems can create meaningful solutions."
        ),
        "form": form,
        "last_login" : last_login, 
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Goeij Angelatika Goeyanto",
        "experience_list": Experience.objects.all(),
        
    }
    
    return render(request, "experience.html", context)


def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Goeij Angelatika Goeyanto",
        "title_query": title_query,
        "form": ProjectForm(),
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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
            raise PermissionDenied
    
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
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Manually build the JSON data so we can add the Star logic
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
                raise PermissionDenied
        
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def show_education(request):
    title_query = request.GET.get("title","").strip()

    context = {
        "name": "Goeij Angelatika Goeyanto",
        "title_query": title_query,
        "form":EducationForm(),
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
                raise PermissionDenied
        
    form = EducationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()

            return JsonResponse(
                {"success": True, "message": "Pendidikan berhasil ditambahkan!"},status=201)

        return JsonResponse(
            {"success": False,"errors": form.errors.get_json_data()},status=400)

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

    data = []
    for edu in education:
        data.append({
            "pk": str(edu.id),
            "fields": {
                "title": edu.title,
                "description": edu.description,
                "year": edu.year,
                "education_url": edu.education_url,
                "education_image_url": edu.education_image_url,
                }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
                raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")


def update_education(request, id):
    education = get_object_or_404(Education, id=id)

    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)

        if form.is_valid():
            form.save()
            return redirect("main:show_education")

    else:
        form = EducationForm(instance=education)

    return render(request, "update_education.html", {
        "form":form,
        "education":education,
    })

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request,"Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name" : "Goeij Angelatika Goeyanto",
        "form" : form,
    }
    return render(request, "register.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Goeij Angelatika Goeyanto",
        "form": form,
    }
    return render(request, "login.html", context)

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)
    return redirect("main:show_projects")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)



@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add education."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Education added successfully.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)