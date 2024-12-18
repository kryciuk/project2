from django.views.generic import TemplateView


class ManagerDashboardView(TemplateView):
    template_name = "dashboards/dashboard_property_manager.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project2 - Property Manager"
        return context
