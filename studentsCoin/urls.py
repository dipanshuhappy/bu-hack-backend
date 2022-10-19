from .views import StudentCoinDetailApiView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('<str:student_professional_detail_id>',view=StudentCoinDetailApiView.as_view(),name='getStudentCoinDetail')
]
# urlpatterns = format_suffix_patterns(urlpatterns)