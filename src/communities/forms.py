from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from communities.models import Building


class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = "__all__"
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "city": _("City"),
            "postal_code": _("Postal code"),
            "street": _("Street"),
            "street_number": _("Building number"),
            "manager": _("Property Manager"),
        }
