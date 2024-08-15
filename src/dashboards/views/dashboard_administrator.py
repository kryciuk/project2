from django.views.generic import TemplateView


class AdministratorDashboardView(TemplateView):
    template_name = "dashboards/dashboard_administrator.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project2 - Administrator"
        return context
