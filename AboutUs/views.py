from django.shortcuts import render

import AboutUs
from AboutUs.models import TeamMember
from Product.models import Product
from django.views.generic import ListView

from home.models import Testimonial, WhyChooseUs


# Create your views here.
class AboutUs(ListView):
    template_name = 'AboutUs/about.html'
    model = Testimonial  # تعریف مدل برای ListView

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = self.object_list  # استفاده از object_list موجود در ListView
        context['features'] = WhyChooseUs.objects.all()
        context['team_members'] = TeamMember.objects.all()
        return context
