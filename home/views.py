from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from Product.models import *
from .models import *
from settingSite.models import FooterLinkBox, SiteSetting
from .forms import NewsletterSubscriptionForm
from django.db.models import Count


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.filter(is_active=True).order_by('-id')[:3]
        context['testimonials'] = Testimonial.objects.all()
        context['best_selling_product'] = (
            Product.objects.annotate(total_sales=Count('id'))
            .order_by('-total_sales')
            [:3]
        )
        we_help_section = WeHelpSection.objects.first()
        context['we_help_section'] = we_help_section
        products = Product.objects.all()
        context['products'] = products
        # Why choose us
        context['features'] = WhyChooseUs.objects.all()
        context['image'] = WhyChooseUsImage.objects.first()

        return context


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'base/site_header_component.html', context)


def site_footer_component(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_success')
    else:
        form = NewsletterSubscriptionForm()

    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()

    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes,
        'form': form
    }
    return render(request, 'base/site_footer_component.html', context)
