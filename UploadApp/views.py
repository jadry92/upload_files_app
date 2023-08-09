# Django
from django.urls import reverse_lazy
from django.views.generic import FormView
# Forms
from UploadApp.forms import FileForm
# Model
from UploadApp.models import File


class FileView(FormView):
    template_name = 'files.html'
    form_class = FileForm
    success_url = reverse_lazy('upload_home')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super(FileView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """adding List"""
        new_kwargs = super(FileView, self).get_context_data(**kwargs)
        new_kwargs['files'] = File.objects.all()
        return new_kwargs

