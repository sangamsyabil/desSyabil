from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView

from carts.models import Cart
from products.models import Product
from .forms import ContactUsForm


class IndexView(ListView):
    paginate_by = 8
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured().order_by('?')


class ContactUsView(View):
    def get(self, *args, **kwargs):
        form = ContactUsForm()
        context = {
            'form': form
        }
        return render(self.request, "moments/contact_us.html", context)

    def post(self, *args, **kwargs):
        form = ContactUsForm(self.request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data.get('full_name')
            sender_email = form.cleaned_data.get('email')
            contact_reason = form.cleaned_data.get('reason')
            sender_message = form.cleaned_data.get('message')

            message = "{} has sent you a new message:\n\n{}".format(sender_name, sender_message)
            send_mail('New Enquiry: {}'.format(contact_reason), message, sender_email, ['syabildesmoments@gmail.com'])

            messages.info(self.request, "We received your message, you will be responded")
            return redirect("moments:home")


# #############################
# Static pages view starts here
# #############################

class ReturnPolicyView(TemplateView):
    template_name = "staticPages/return_policy.html"


class AboutUsView(TemplateView):
    template_name = "staticPages/about_us.html"


class JobOpeningsView(TemplateView):
    template_name = "moments/vacancies.html"


class PrivacyPolicyView(TemplateView):
    template_name = "staticPages/privacy_policy.html"


class CookiePolicyView(TemplateView):
    template_name = "staticPages/cookie_policy.html"


class DeliveryInfoView(TemplateView):
    template_name = "staticPages/delivery_info.html"


class TermsView(TemplateView):
    template_name = "staticPages/terms_and_condition.html"


class FaqView(TemplateView):
    template_name = "staticPages/faq.html"


class TradeShowsView(TemplateView):
    template_name = "staticPages/trade_shows.html"


class FontTestView(TemplateView):
    template_name = "staticPages/font_tests.html"
