from django.contrib import admin
from django import forms
#from mptt.forms import TreeNodeMultipleChoiceField
from django.contrib.auth.models import User
from .models import Project
from .models import Backlog
from .models import Sprint

# Register your models here.

'''class ProjectAdminForm(forms.ModelForm):
    members = TreeNodeMultipleChoiceField(required=False,
                                          queryset = User.objects.all(),
                                          level_indicator = u'+--',
                                          widget = admin.widgets.FilteredSelectMultiple('Members', False))
    class Meta:
        model = Project
        fields = '__all__'

class ToppingAdminForm(forms.ModelForm):
  pizzas = forms.ModelMultipleChoiceField(
    queryset=Pizza.objects.all(), 
    required=False,
    widget=FilteredSelectMultiple(
      verbose_name=_('Pizzas'),
      is_stacked=False
    )
  )

  class Meta:
    model = Topping

  def __init__(self, *args, **kwargs):
    super(ToppingAdminForm, self).__init__(*args, **kwargs)

    if self.instance and self.instance.pk:
      self.fields['pizzas'].initial = self.instance.pizzas.all()

  def save(self, commit=True):
    topping = super(ToppingAdminForm, self).save(commit=False)

    if commit:
      topping.save()

    if topping.pk:
      topping.pizzas = self.cleaned_data['pizzas']
      self.save_m2m()

    return topping
'''
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_members', 'start','finish', 'status', 'owner', 'target_estimate')
    search_fields = ('title','status')
    #raw_id_fields = ('title',)
    list_filter = ('status','start', 'owner')
    date_hierarchy = 'start'
    prepopulated_fields={'slug':('title',)}
    ordering = ['start']
    filter_horizontal = ('members',)

class BacklogAdmin(admin.ModelAdmin):
    list_display = ('title', 'btype', 'project_name', 'sprint_name', 'dateadded', 'priority', 'status')
    search_fields = ('project_name', 'title', 'dateadded', 'priority')
    #raw_id_fields = ('title',)
    list_filter = ('title', 'dateadded', 'sprint_name', 'priority', 'status')
    date_hierarchy = 'dateadded'
    prepopulated_fields={'slug':('title',)}
    ordering = ['dateadded']

class SprintAdmin(admin.ModelAdmin):
    list_display = ('title','dateadded','days', 'project_title', 'gap')
    search_fields = ('title','project_title')
    #raw_id_fields = ('title',)
    list_filter = ('title','project_title', 'days')
    date_hierarchy = 'dateadded'
    prepopulated_fields={'slug':('title',)}
    ordering = ['dateadded']

admin.site.register(Project, ProjectAdmin,)
admin.site.register(Backlog, BacklogAdmin,)
admin.site.register(Sprint, SprintAdmin,)
