from .views import MakeTransaction,GetTransactions,UploadExcel,MakeAlphaCoinRequest,GetAlphaCoinRequest,ListAlphaCoinRequest,VerifyRequest;
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('make-transaction',view=MakeTransaction.as_view(),name='putTranstion'),
    path('',view=GetTransactions.as_view(),name="get_transactions"),
    path('upload-file',UploadExcel.as_view(),name="excel-parsing"),
    path('request/',view=MakeAlphaCoinRequest.as_view(),name='create_transaction_request'),
    path('request/<int:pk>',view=GetAlphaCoinRequest.as_view()),
    path('requests/',view =ListAlphaCoinRequest.as_view()),
    path('verify-request',view=VerifyRequest.as_view(),name="verify alpha coin request")
]
# urlpatterns = format_suffix_patterns(urlpatterns)