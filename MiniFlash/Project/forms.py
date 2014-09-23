from django.forms import ModelForm
from models import Project, UserProjectRelation

class ProjectForm(ModelForm):
    class Meta:
		model = Project
		fields = ['name']

    def save(self, *args, **kwargs):
        project = super(ProjectForm, self).save(*args, **kwargs)
        relation = UserProjectRelation(user=self.user, project=project, role='1')
        relation.save()
        return project

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProjectForm, self).__init__(*args, **kwargs)