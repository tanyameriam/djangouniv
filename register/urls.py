from django.conf.urls import url
from register.views import *

urlpatterns = [
    url(r'^signup/$', UserRegistrationView.as_view(),name='signup'),
]