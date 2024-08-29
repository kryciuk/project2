import os

from django.conf import settings
from django.http import FileResponse, Http404
from django.utils.http import content_disposition_header
from django.views import View


class BuildingQRDownloadView(View):
    def get(self, request, id_building, filename):
        file_path = os.path.join(settings.MEDIA_ROOT, f"building{id_building}_qrcode.png")
        if not os.path.exists(file_path):
            raise Http404("Nie znaleziono pliku.")
        response = FileResponse(open(file_path, "rb"))
        response["Content-Disposition"] = content_disposition_header(as_attachment="attachment", filename=filename)
        return response
