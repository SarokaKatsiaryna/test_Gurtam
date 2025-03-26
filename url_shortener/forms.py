from django import forms
from url_shortener.models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ("long_url", "time_to_live")
        labels = {
            "long_url": "Enter your link",
            "time_to_live": "Enter the lifetime of the link (in days)",
        }
        widgets = {
            "long_url": forms.TextInput(attrs={"style": "width: 300px"}),
            "time_to_live": forms.NumberInput(attrs={"style": "width: 300px"}),
        }
