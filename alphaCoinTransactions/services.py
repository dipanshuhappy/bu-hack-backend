from __future__ import annotations
from studentsCoin.models import StudentCoinDetail
from .models import AlphaTransaction,AlphaRequestTransaction
from datetime import datetime, timedelta
from rest_framework.authtoken.models import Token
from staffs.models import StaffProfessionalDetails
from students.models import StudentProfessionalDetails
from django.db.models import QuerySet
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .serializers import AlphaTransactionListQuerySerializer
def is_sender_same_batch_with_receiver(sender_id:str,receiver_id:str)->bool:
    print("reciever id",receiver_id)
    print("sender_id",sender_id)
    student_batch = StudentProfessionalDetails.objects.get(bennett_email=receiver_id).batch
    staff_batch = StaffProfessionalDetails.objects.get(bennett_email=sender_id).batch_mentor
    return student_batch==staff_batch
def is_sender_id_valid(token:str,sender_id:str)->bool:
    user:str = Token.objects.get(pk=token).user
    sender_email:str = StaffProfessionalDetails.objects.get(bennett_email=sender_id).bennett_email
    return str(user) == sender_email.split("@")[0]
def addAlphaCoinToStudent(student_email:str,amount:int):
    studentCoin = StudentCoinDetail.objects.get(student_professional_detail_id=student_email)
    studentCoin.alpha_coin+=amount
    studentCoin.save(update_fields=["alpha_coin"])
def get_queryset_by_time_period(query:AlphaTransactionListQuerySerializer,by:str)->QuerySet:
        end_date=datetime.now()
        if(query.data.get("time_period")=="week"):
            return AlphaTransaction.objects.filter(**{by:query.data[by]}).filter(current_timestamp__gte=datetime.now()-timedelta(days=7),current_timestamp__lte=end_date)
        elif(query.data.get("time_period")=="month"):
            return AlphaTransaction.objects.filter(**{by:query.data[by]}).filter(current_timestamp__gte=datetime.now()-timedelta(days=25),current_timestamp__lte=end_date)
def get_queryset_by_time_period_and_lastest(query:AlphaTransactionListQuerySerializer,by:str,number_of_results:int=5):  return get_queryset_by_time_period(query,by).order_by('-current_timestamp')[:number_of_results]
def get_queryset_by_lastest(query:AlphaTransactionListQuerySerializer,by:str,number_of_results:int=5): return AlphaTransaction.objects.filter(**{by:query.data[by]}).order_by('-current_timestamp')[:number_of_results]
def get_request_queryset(query:AlphaTransactionListQuerySerializer,by:str,is_valid:bool):
    print(by)
    return AlphaRequestTransaction.objects.filter(**{by:query.data[by]}).filter(is_valid=is_valid).order_by('-current_timestamp')