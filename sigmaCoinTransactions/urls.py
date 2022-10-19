from .views import MakeTransaction,GetTransactions,UploadExcel;
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('make-transaction',view=MakeTransaction.as_view(),name='putTranstion'),
    path('',view=GetTransactions.as_view(),name="get_transactions"),
    path('upload-file',UploadExcel.as_view(),name="excel-parsing"),
    #path('request/',view=MakeSigmaCoinRequest.as_view(),name='create_transaction_request'),
    #path('request/<int:pk>',view=GetSigmaCoinRequest.as_view()),
   # path('requests/',view =ListSigmaCoinRequest.as_view()),
   # path('verify-request',view=VerifyRequest.as_view(),name="verify sigma coin request")
]
urlpatterns = format_suffix_patterns(urlpatterns)