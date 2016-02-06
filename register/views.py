from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin#we need some files that the logins only should see eg sign in page here anonymouus only could see if deleted the signed in could see
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from register.forms import *

class Home(TemplateView):
    template_name = "index.html"


class UserRegistrationView(AnonymousRequiredMixin, FormView):#this is standard code :)
    template_name = "signup.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/register/user/success/'#which page should go after sign in

    def form_valid(self, form):
      form.save()
      return FormView.form_valid(self, form)