from django.views import generic

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'home/home.html'


class ImpressumView(generic.TemplateView):
    template_name = 'legal/impressum.html'
