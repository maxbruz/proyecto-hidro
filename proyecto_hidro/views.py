from django.views.generic import TemplateView

class Landing(TemplateView):
    template_name="page/landing_page.html"
class Contact(TemplateView):
    template_name="page/contacto.html"
class QuienesSomos(TemplateView):
    template_name="page/quienesSomos.html"
class sales(TemplateView):
    template_name="page/sales.html"
class show_data(TemplateView):
    template_name="page/show_data.html"