from django.forms import ModelForm

from communities.models import Building


class BuildingForm(ModelForm):

    class Meta:
        model = Building
        fields = "__all__"
