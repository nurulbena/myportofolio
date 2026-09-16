from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import SkillForm
from main.models import Experience, Skill

def show_main(request):
    context = {
        "name": "Nurul Fikryati Bena",
        "npm": "2506534825",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia with a strong interest in programming, digital technology and design."
            "Experienced in working both independently and collaboratively in team environments."
            "Highly motivated to continue learning and developing skills in technology, visual design, and multimedia creation."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nurul Fikryati Bena",
        "experience_list": Experience.objects.all(),
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

def create_skill(request):
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

    skills_json = serializers.serialize("json", skills)
    return HttpResponse(skills_json, content_type="application/json")

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skills")

    return redirect("main:show_skills")