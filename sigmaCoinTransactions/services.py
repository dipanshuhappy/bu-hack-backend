from studentsCoin.models import StudentCoinDetail
from staffs.models import StaffProfessionalDetails
from staffCoins.models import StaffCoinDetails
from datetime import datetime, timedelta
from .models import SigmaTransaction
from rest_framework.authtoken.models import Token
from django.db.models import QuerySet
from .serializers import SigmaTransactionSerializer
# if TYPE_CHECKING:
#     from .serializers import SigmaTransactionListQuerySerializer
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
def add_sigma_coin_to_student(student_email:str,amount:int):
    studentCoin = StudentCoinDetail.objects.get(student_professional_detail_id=student_email)
    studentCoin.sigma_coin+=amount
    studentCoin.save(update_fields=["sigma_coin"])  
def remove_sigma_coin_from_staff(staff_email:str,amount:int):
    staffCoin=StaffCoinDetails.objects.get(staff_professional_detail_id=staff_email)
    staffCoin.sigma_coin-=amount
    staffCoin.save(update_fields=["sigma_coin"]) 
def staff_has_insufficent_balance(sender_id:str,amount:int):
    staffCoin=StaffCoinDetails.objects.get(staff_professional_detail_id=sender_id)
    if(staffCoin.sigma_coin<amount):
        return True;
    return False;
def get_queryset_by_time_period(query:SigmaTransactionSerializer,by:str)->QuerySet:
        end_date=datetime.now()
        if(query.data.get("time_period")=="week"):
            return SigmaTransaction.objects.filter(**{by:query.data[by]}).filter(current_timestamp__gte=datetime.now()-timedelta(days=7),current_timestamp__lte=end_date)
        elif(query.data.get("time_period")=="month"):
            return SigmaTransaction.objects.filter(**{by:query.data[by]}).filter(current_timestamp__gte=datetime.now()-timedelta(days=25),current_timestamp__lte=end_date)
def get_queryset_by_time_period_and_lastest(query:SigmaTransactionSerializer,by:str,number_of_results:int=5):  return get_queryset_by_time_period(query,by).order_by('-current_timestamp')[:number_of_results]
def get_queryset_by_lastest(query:SigmaTransactionSerializer,by:str,number_of_results:int=5): return SigmaTransaction.objects.filter(**{by:query.data[by]}).order_by('-current_timestamp')[:number_of_results]

