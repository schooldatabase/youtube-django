from django.urls import path
from .views import *

urlpatterns = [
    # urls file
    # path('convert/', convert_file, name='convert_file'),
    # path('converted/', converted_files, name='converted_files'),
    path('convert/', FileConversionView.as_view(), name='file_conversion'),
]


