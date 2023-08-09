# django
from django.db import models
# utils
import re


def extension_directory_path(instance, filename):
    extension_search = re.search('^.*\.([a-z]{1,})$', filename)
    if extension_search:
        extension = extension_search.group(1)
        return 'files/{0}/{1}'.format(extension, filename)


class File(models.Model):
    """
    File

    This is the model for the data base
    """
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to=extension_directory_path)
    size = models.PositiveBigIntegerField()
    uploaded = models.DateField(auto_now=True)