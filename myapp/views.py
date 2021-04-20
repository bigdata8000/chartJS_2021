from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club


class ClubChartView(TemplateView):
    template_name = 'myapp/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Club.objects.all()
        return context



class ClubChartView2(TemplateView):
    template_name = 'myapp/chart2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Club.objects.all()
        return context

