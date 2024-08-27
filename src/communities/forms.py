from django.forms import ModelForm

from communities.models import Building


class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = "__all__"
        labels = {
            "name": "Nazywa",
            "description": "Opis",
            "city": "Miasto",
            "postal_code": "Kod pocztowy",
            "street": "Ulica",
            "street_number": "Numer budynku",
            "manager": "Zarządca",
        }
