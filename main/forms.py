from django.forms import ModelForm, TextInput, Textarea, Select

from main.models import Skill

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