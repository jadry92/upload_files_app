
# Django
from django.urls import path
# View
from UploadApp.views import FileView

urlpatterns = [
    path('', view=FileView.as_view(), name='upload_home'),
]
