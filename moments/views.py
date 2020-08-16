from django.views.generic import ListView, DetailView, View, TemplateView


class IndexView(ListView):
    template_name = "home_page.html"

    def get_queryset(self):
        pass


# #############################
# Static pages view starts here
# #############################

class ReturnPolicyView(TemplateView):
    template_name = "staticPages/return_policy.html"


class ContactUsView(TemplateView):
    template_name = "staticPages/return_policy.html"


class PrivacyPolicyView(TemplateView):
    template_name = "staticPages/privacy_policy.html"


class CookiePolicyView(TemplateView):
    template_name = "staticPages/cookie_policy.html"


class DeliveryPolicyView(TemplateView):
    template_name = "staticPages/delivery_policy.html"


class TermsView(TemplateView):
    template_name = "staticPages/terms_and_condition.html"


class FaqView(TemplateView):
    template_name = "staticPages/faq.html"


class TradeShowsView(TemplateView):
    template_name = "staticPages/trade_shows.html"


class FontTestView(TemplateView):
    template_name = "staticPages/font_tests.html"
