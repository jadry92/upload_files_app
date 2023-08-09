# Django
from django import forms
from django.forms import ModelForm, ValidationError
# Model
from UploadApp.models import File
# Utils
import re

MAX_DOCUMENT_SIZE = 5*(1024**2)

DOCUMENT_FORMATS = ['pdf', 'docx', 'txt']


class FileForm(ModelForm):
    """
    File Form

    This form to parser the data to model and make the validation of the files.

    Validations :
    - size : no more than 5MB
    - formats accepted : .pdf .docx

    """
    class Meta:
        model = File
        fields = ['file', 'name', 'size']
        exclude = ['name', 'size']

    def clean(self):

        file = self.cleaned_data['file']
        if file.size > MAX_DOCUMENT_SIZE:
            raise ValidationError('The File has to be less than 5MB')

        search_ext = re.search('^.*\.([a-z]{1,})$', file.name)
        if search_ext:
            if not (search_ext.group(1) in DOCUMENT_FORMATS):
                raise ValidationError(
                    'File has to be {}'.format(DOCUMENT_FORMATS))
        else:
            raise ValidationError('File has no extension')

        return self.cleaned_data

    def save(self, commit=True):

        instance = super(FileForm, self).save(commit=False)
        file = self.cleaned_data['file']
        instance.name = file.name
        instance.size = file.size
        if commit:
            instance.save()
        return instance