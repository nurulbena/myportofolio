from django.shortcuts import render

from main.models import Experience, Skill


def show_main(request):
    context = {
        "name": "Nurul Fikryati Bena",
        "npm": "2506534825",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Iformation Systems student at Universitas Indonesia with a strong interest in programming, digital technology and design."
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
    context = {
        "name": "Nurul Fikryati Bena",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skills.html", context)