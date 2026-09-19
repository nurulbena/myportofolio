from django.forms import ModelForm, TextInput, Textarea, Select, URLInput

from main.models import Skill, Experience

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "name",
            "description",
            "category",
        ]

        labels = {
            "name": "Nama Skill",
            "description": "Deskripsi",
            "category": "Kategori",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Video Editing",
                    "maxlength": 100,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan skill kamu",
                    "rows": 3,
                }
            ),
            "category": Select(),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Judul",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "Link Gambar (opsional)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Staff of Software Engineering Academy",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalaman kamu",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
        }