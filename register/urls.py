from django.conf.urls import url
from register.views import *

urlpatterns = [
    url(r'^signup/$', UserRegistrationView.as_view(),name='signup'),
    url(r'^user/success/$', UserRegistrationSuccessView.as_view(),name='success'),
    url(r'^dash/$', UserDashboardView.as_view(),name='dash'),


]