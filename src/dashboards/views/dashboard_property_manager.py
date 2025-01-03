from django.views.generic import TemplateView


class ManagerDashboardView(TemplateView):
    template_name = "dashboards/dashboard_property_manager.html"
    extra_context = {"title": "Project2 - Property Manager"}
