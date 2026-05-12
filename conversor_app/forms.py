from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

def validate_file_size(value):
    """
    Valida que el archivo subido no supere los 10MB.
    El tamaño del archivo (value.size) viene en bytes.
    """
    limit = 10 * 1024 * 1024  # 10 MB en bytes
    if value.size > limit:
        raise ValidationError('El archivo es demasiado grande. El tamaño máximo permitido es de 10MB.')

class CSVUploadForm(forms.Form):
    file = forms.FileField(
        label='Sube tu archivo CSV',
        validators=[
            FileExtensionValidator(allowed_extensions=['csv']),
            validate_file_size
        ]
    )

class PDFUploadForm(forms.Form):
    file = forms.FileField(
        label='Sube tu archivo PDF',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf']),
            validate_file_size
        ]
    )