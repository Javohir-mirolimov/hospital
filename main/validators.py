from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import re
from django.core.validators import RegexValidator

class ImageFileValidator(FileExtensionValidator):
    def __init__(self, allowed_extension=None, message=None):
        self.allowed_extensions = allowed_extension or ['jpg' , 'jpeg', 'png', 'gif', 'bmd']
        self.message = message or 'File must be an image with a valid extansion'

    def __call__(self, value):
        # Get the file extension using a regular expression
        match = re.search(r'\.([a-zA-Z0-9]+)$', str(value))
        if not match or match.group(1).lower() not in self.allowed_extensions:
            raise ValidationError(self.message, code='invalid')



class LinkValidator(RegexValidator):
    def __init__(self, message=None):
        regex = (
            r'^(http|https)://'
            r'([a-zA-Z0-9,-]+)'
            r'(\.[a-Za-Z]{2,})'
            r'(/[^\s]*)?$'
        )
        self.message = message or 'Enter a valid link'
        super().__init__(regex)



class AudioFilevalodator(FileExtensionValidator):
    def __int__(self, allowed_extensions=None, message=None):
        self.allowed_extensions = allowed_extensions or ['mp3', 'wav', 'ogg', 'flac']
        self.message = message or 'File must be an audio file with a valid extension'
        super().__int__(allowed_extensions=self.allowed_extensions, message=self.message)


    def __call__(self, value):
        # Example: Using a regular expression to check the file name
        match = re.search(r'\.([a-zA-Z0-9]+)$', str(value))
        if not match or match.group(1).lower() not in self.allowed_extensions:
            raise ValidationError(self.message , code='invalid')


