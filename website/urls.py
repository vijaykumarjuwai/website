from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='website/index.html'), name='index'),
    url(r'^contact$', TemplateView.as_view(template_name='website/contact.html'), name='contact'),
]