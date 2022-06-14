from django.shortcuts import render
from django.views.generic import TemplateView



class Template1(TemplateView):
    template_name = "p2p/index.html"


class Template2(TemplateView):
    template_name = "nima/index.html"