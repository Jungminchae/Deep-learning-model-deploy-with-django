from App.models import FileModel
from django.forms import ModelForm


class FileForm(ModelForm):
    """
    Creating a form that maps to the model: https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/
    This form is used for the file upload.
    """
    class Meta:
        model = FileModel
        fields = ['file']
