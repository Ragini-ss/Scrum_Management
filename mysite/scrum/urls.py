from django.conf.urls import url, include, patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    
    
    # login / logout urls
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    # change password urls
    url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),

    # url(r'^(?P<slug>[\w-]+)/$', views.ProjectDetailView.as_view(), name='project_detail'),

    url(r'^myprojects/$', views.ManageProjectListView.as_view(),name = 'manage_project_list'),
    url(r'^create/$', views.ProjectCreateView.as_view(),name = 'project_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.ProjectUpdateView.as_view(),name = 'project_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.ProjectDeleteView.as_view(),name = 'project_delete'),
]
 # 
    #url(r'^register/$', views.register, name='register'),
    #url(r'^edit/$', views.edit, name='edit'),

