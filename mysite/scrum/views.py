from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from forms import LoginForm
from django.views.generic.list import ListView
from .models import Project
from django.views.generic.detail import DetailView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

'''class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project/detail.html'
    success_url = reverse_lazy('project_detail')
'''
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'projects/manage/project/list.html', {'section': 'dashboard'})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request,
                  'dashboard.html',
                  {'section': 'dashboard'})

class MemberMixin(object):
    def get_queryset(self):
        qs = super(MemberMixin, self).get_queryset()
        return qs.filter(members = self.request.user)

class MemberEditMixin(object):
    def form_valid(self, form):
        form.instance.members = self.request.user
        return super(MemberEditMixin, self).form_valid(form)

class MemberProjectMixin(MemberMixin, LoginRequiredMixin):
    model = Project
    fields = ['title', 'slug', 'finish', 'status', 'target_estimate']
    success_url = reverse_lazy('manage_project_list')

class MemberProjectEditMixin(MemberProjectMixin, MemberEditMixin):
    fields = ['title', 'slug', 'finish', 'status', 'target_estimate']
    success_url = reverse_lazy('manage_project_list')
    template_name = 'projects/manage/project/form.html'

class ManageProjectListView(MemberProjectMixin, ListView):
    template_name = 'projects/manage/project/list.html'

class ProjectCreateView(PermissionRequiredMixin, MemberProjectEditMixin, CreateView):
    permission_required = 'scrum.add_project'

class ProjectUpdateView(PermissionRequiredMixin, MemberProjectEditMixin, UpdateView):
    template_name = 'projects/manage/project/form.html'
    permission_required = 'scrum.change_project'

class ProjectDeleteView(PermissionRequiredMixin, MemberProjectEditMixin, DeleteView):
    template_name = 'projects/manage/project/delete.html'
    success_url = reverse_lazy('manage_project_list')
    permission_required = 'scrum.delete_project'




















        
