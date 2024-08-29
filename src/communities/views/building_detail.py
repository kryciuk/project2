import os

import qrcode as qr
from django.contrib.sites.models import Site
from django.urls import reverse
from django.views.generic import DetailView
from PIL import Image, ImageDraw

from communities.models import Building
from core import settings


class BuildingDetailView(DetailView):
    template_name = "communities/building_detail.html"
    context_object_name = "building"
    model = Building

    def get(self, request, *args, **kwargs):
        self.create_issue_report_qr_code()
        request.session["id_building"] = kwargs.get("id_building")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def create_issue_report_qr_code(self):
        building_id = self.kwargs.get("pk")
        current_site = Site.objects.get_current()
        url = reverse("issue-report", kwargs={"id_building": building_id})

        qrcode = qr.make(f"{current_site.domain}{url}")
        canvas = Image.new("RGB", (600, 600), "white")
        ImageDraw.Draw(canvas)
        qr_width, qr_height = qrcode.size
        paste_position = ((600 - qr_width) // 2, (600 - qr_height) // 2)
        canvas.paste(qrcode, paste_position)

        file_name = f"building{building_id}_qrcode.png"
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        canvas.save(file_path)
        canvas.close()
