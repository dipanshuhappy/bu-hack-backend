from .views import StaffCoinDetailApiView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('<str:staff_professional_detail_id>',view=StaffCoinDetailApiView.as_view(),name='getStaffCoinDetail')
]
# urlpatterns = format_suffix_patterns(urlpatterns)