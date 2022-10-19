from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('<str:bennett_email>',view=views.StaffDetailsApiView.as_view(),name='getStaffId')
]
# urlpatterns = format_suffix_patterns(urlpatterns)