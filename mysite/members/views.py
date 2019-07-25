from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from braces.views import LoginRequiredMixin
from .forms import ProjectAssignmentForm

'''class MemberAssignProjectView(LoginRequiredMixin, FormView):
    project = None
    form_class = ProjectAssignmentForm

    def form_valid(self, form):
        self.project = form.cleaned_data['project']
        self.project.members.add(self.request.user)
        return super(MemberAssignProjectView,
                     self).form_valid(form)

   # def get_success_url(self):
    #    return reverse_lazy('member_project_detail',
     #                       args = [self.project.id])
        # pass
'''
