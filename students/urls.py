from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('<str:bennett_email>',view=views.StudentDetailApiView.as_view(),name='getStudentId')
]
# urlpatterns = format_suffix_patterns(urlpatterns)
