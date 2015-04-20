from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Presentation


# Create your views here.
class PresentationView(TemplateView):
    template_name = "presentations/presentation.html"

    def get_context_data(self, **kwargs):
        context = super(PresentationView, self).get_context_data(**kwargs)
        presentation = Presentation.objects.get(slug=kwargs['slug'])

        context['presentation'] = presentation
        return context