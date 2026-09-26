import datetime

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from main.forms import SkillForm, ExperienceForm
from main.models import Experience, Skill

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Nurul Fikryati Bena",
        "npm": "2506534825",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia with a strong interest in programming, digital technology and design."
            "Experienced in working both independently and collaboratively in team environments."
            "Highly motivated to continue learning and developing skills in technology, visual design, and multimedia creation."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nurul Fikryati Bena",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_skills(request):
    json_response = get_skills_json(request)

    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]
    name_query = request.GET.get("name", "").strip()

    context = {
        "name": "Nurul Fikryati Bena",
        "skill_list": skills,
        "name_query": name_query,
    }
    return render(request, "skills.html", context)

@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skills")

    context = {
        "name": "Nurul Fikryati Bena",
        "form": form,
    }
    return render(request, "skills_form.html", context)

def get_skills_json(request):
    name_query = request.GET.get("name", "").strip()
    skills = Skill.objects.all()

    if name_query:
        skills = skills.filter(name__icontains=name_query)

    skills_json = serializers.serialize(
        "json", skills, use_natural_foreign_keys=True
)
    return HttpResponse(skills_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skills")

    return redirect("main:show_skills")

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Nurul Fikryati Bena",
        "form": form,
        "is_edit": False,
        "form_action": reverse("main:create_experience"),
    }
    return render(request, "experience_form.html", context)

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diupdate!")
        return redirect("main:show_experience")

    context = {
        "name": "Nurul Fikryati Bena",
        "form": form,
        "is_edit": True,
        "form_action": reverse("main:update_experience", args=[experience_id]),
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Nurul Fikryati Bena",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Nurul Fikryati Bena",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        if request.user in skill.starred_by.all():
            skill.starred_by.remove(request.user)
        else:
            skill.starred_by.add(request.user)

    return redirect("main:show_skills")