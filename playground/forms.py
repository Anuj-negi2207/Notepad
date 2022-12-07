from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    heading = forms.CharField(
                required=True, 
                widget= forms.widgets.Textarea(
                    attrs={ 
                        "placeholder": "Add a heading note",
                    }
                ),
                label=""
                )

    body = forms.CharField(
                required=True,
                widget= forms.widgets.Textarea(
                    attrs={ 
                        "placeholder": "Add your note here",
                        "class": "textarea is-success is-medium"
                    }
                ),
                label="")

    class Meta:
        model = Note
        exclude = ("user", )