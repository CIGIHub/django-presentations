from django.conf.urls import patterns, url
from presentations.views import PresentationView

urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$', PresentationView.as_view(), name='presentation'),
    # url(r'^$', PresentationView.as_view(), name='presentation'),
)