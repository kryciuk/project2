from django.views.generic import TemplateView


class AdministratorDashboardView(TemplateView):
    template_name = "dashboards/dashboard_administrator.html"
    extra_context = {"title": "Project2 - Administrator"}
