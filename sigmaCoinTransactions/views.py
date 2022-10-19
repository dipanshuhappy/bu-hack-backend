from datetime import datetime, timedelta
from rest_framework import generics
from .serializers import SigmaTransactionSerializer,SigmaTransactionListQuerySerializer,ExcelFileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import SigmaTransaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from .services import staff_has_insufficent_balance,is_sender_id_valid,add_sigma_coin_to_student,remove_sigma_coin_from_staff,get_queryset_by_lastest,get_queryset_by_time_period,get_queryset_by_time_period_and_lastest
class MakeTransaction(APIView):
        queryset=SigmaTransaction.objects.all()
        serializer_class=SigmaTransactionSerializer
        authentication_classes=[TokenAuthentication]
        permission_classes=[IsAuthenticated]
        def post(self,request):
            serializer = SigmaTransactionSerializer(data=request.POST);
            if serializer.is_valid(raise_exception=True):
                sender_id=serializer.validated_data["sender_id"]
                receiver_id=serializer.validated_data["receiver_id"]
                amount=serializer.validated_data["amount"]
                if(not is_sender_id_valid(request.auth,sender_id)):
                    return Response({"detail":"You don't have access to make this transaction"},status=401)
                if(staff_has_insufficent_balance(sender_id,amount)):
                    return Response({"detail":"User does not have enough sigma coin to make this transaction"})
                add_sigma_coin_to_student(receiver_id,amount)
                remove_sigma_coin_from_staff(sender_id,amount)
                serializer.save()
                return Response(serializer.data,status=200)
            else:
                return Response("Transtionsaction is not valid",status=500)
class GetTransactions(generics.ListAPIView):
    serializer_class=SigmaTransactionSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        query = SigmaTransactionListQuerySerializer(data=self.request.query_params)
        if(query.is_valid(raise_exception=True)):
            if(query.data.get("sender_id")!=None):
                by="sender_id"
                if(query.data.get("latest") and query.data.get("time_period")!=None):
                   return get_queryset_by_time_period_and_lastest(query,by)
                if(query.data.get("latest")):
                    return get_queryset_by_lastest(query,by)
                if(query.data.get("time_period")!=None):
                    return get_queryset_by_time_period(query,by)
                
            elif(query.data.get("receiver_id")!=None):
                by="receiver_id"
                if(query.data.get("latest") and query.data.get("time_period")!=None):
                   return get_queryset_by_time_period_and_lastest(query,by)
                if(query.data.get("latest")):
                    return get_queryset_by_lastest(query,by)
                if(query.data.get("time_period")!=None):
                    return get_queryset_by_time_period(query,by)
                
        return SigmaTransaction.objects.none()
class UploadExcel(APIView):
    serializer_class=ExcelFileSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self, request, *args, **kwargs):
        file = ExcelFileSerializer(data=request.data)
        if file.is_valid(raise_exception=True):
            excel:InMemoryUploadedFile=file.validated_data["file"]
            extension = excel.name.split(".")[-1]
            content = excel.read()
            sheet = pyexcel.get_sheet(file_type=extension, file_content=content,name_columns_by_row=0).to_dict()
            max_mark=max(sheet["marks"])
            min_mark=min(sheet["marks"])
            sender_id=file.validated_data["sender_id"]
            for enrollment_id,mark in zip(sheet["enrollment_id"],sheet["marks"]):
                amount = getCoinAmount(min_mark,max_mark,int(mark),10)
                transaction= SigmaTransactionSerializer(data={
                    "sender_id":sender_id,
                    "receiver_id":enrollment_id+"@bennett.edu.in",
                    "amount":amount
                })
                if transaction.is_valid(raise_exception=True):
                    addSigmaCoinToStudent(
                        enrollment_id+"@bennett.edu.in",
                        amount
                    )
                transaction.save()
            return Response({"detail":"Transaction Complete"}, status=status.HTTP_201_CREATED)
        return Response({"detail":"Try your transaction again"},status=status.HTTP_408_REQUEST_TIMEOUT)
