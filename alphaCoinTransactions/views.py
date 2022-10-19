from re import L
from rest_framework import generics
from .serializers import AlphaTransactionSerializer,AlphaTransactionListQuerySerializer,ExcelFileSerializer,AlphaRequestTransactionSerializer,AlphaRequestTransactionGetSerializer,TransactionResultsQuerySerializer,VerifyTransactionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import AlphaTransaction,AlphaRequestTransaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.uploadedfile import InMemoryUploadedFile
from .services import addAlphaCoinToStudent,get_queryset_by_lastest,get_queryset_by_time_period,get_queryset_by_time_period_and_lastest,is_sender_id_valid,get_request_queryset
from .utils import getCoinAmount
import pyexcel

class MakeTransaction(APIView):
        queryset=AlphaTransaction.objects.all()
        serializer_class=AlphaTransactionSerializer
        authentication_classes=[TokenAuthentication]
        permission_classes=[IsAuthenticated]
        def post(self,request):
            serializer = AlphaTransactionSerializer(data=request.POST);
            if serializer.is_valid(raise_exception=True):
                if (is_sender_id_valid(request.auth,serializer.validated_data["sender_id"])):
                    return Response(data={"message":"User is not authorized for this transaction"},status=500)
                addAlphaCoinToStudent(serializer.validated_data["receiver_id"],serializer.validated_data["amount"])
                return Response(serializer.data,status=200)
            else:
                return Response(status=500)
class GetTransactions(generics.ListAPIView):
    serializer_class=AlphaTransactionSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        query = AlphaTransactionListQuerySerializer(data=self.request.query_params)
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
        return AlphaTransaction.objects.none()
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
                transaction= AlphaTransactionSerializer(data={
                    "sender_id":sender_id,
                    "receiver_id":enrollment_id+"@bennett.edu.in",
                    "amount":amount
                })
                if transaction.is_valid(raise_exception=True):
                    addAlphaCoinToStudent(
                        enrollment_id+"@bennett.edu.in",
                        amount
                    )
                transaction.save()
            return Response({"detail":"Transaction Complete"}, status=status.HTTP_201_CREATED)
        return Response({"detail":"Try your transaction again"},status=status.HTTP_408_REQUEST_TIMEOUT)
class MakeAlphaCoinRequest(APIView):
    queryset=AlphaRequestTransaction.objects.all()
    serializer_class=AlphaRequestTransactionSerializer
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return AlphaRequestTransactionSerializer
        return 
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    def post(self, request, *args, **kwargs):
        post_dict=request.POST.dict();
        print(request.FILES)
        post_dict["file"]= request.FILES['file'] if request.FILES.get('file')!=None else None
        # request.POST['file']=request.FILES['file']
        alphaRequest = AlphaRequestTransactionSerializer(data=post_dict)
        if(alphaRequest.is_valid(raise_exception=True)):
            alphaRequest.save();
            return Response(alphaRequest.data,status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"Request  Not Complete"}, status=status.HTTP_400_BAD_REQUEST)
class GetAlphaCoinRequest(generics.RetrieveAPIView):
    queryset=AlphaRequestTransaction.objects.all()
    serializer_class=AlphaRequestTransactionGetSerializer
    lookup_field = 'pk'
class ListAlphaCoinRequest(generics.ListAPIView):
    serializer_class=AlphaRequestTransactionGetSerializer
    def get_queryset(self):
        query=TransactionResultsQuerySerializer(data=self.request.query_params)
        
        if(query.is_valid(raise_exception=True)):
            print(query.data)
            if(query.data.get("sender_id")!=None):
                return get_request_queryset(query,"sender_id",True) if query.data.get("is_valid") else get_request_queryset(query,"sender_id",False)
            if(query.data.get("receiver_id")!=None):
                return get_request_queryset(query,"receiver_id",True) if query.data.get("is_valid") else get_request_queryset(query,"receiver_id",False)
        return AlphaRequestTransaction.objects.none();
class VerifyRequest(APIView):
    serializer_class=VerifyTransactionSerializer
    def post(self, request, *args, **kwargs):
        serializer=VerifyTransactionSerializer(data=request.POST)
        if(serializer.is_valid(raise_exception=True)):
            alphaRequest=AlphaRequestTransaction.objects.get(pk=serializer.data["id"])
            alphaRequest.is_valid=True;
            alphaRequest.save()
            transaction= AlphaTransactionSerializer(data={
                    "sender_id":alphaRequest.sender_id,
                    "receiver_id":alphaRequest.receiver_id,
                    "amount":alphaRequest.amount,
                    "message":alphaRequest.message
            })
            if transaction.is_valid(raise_exception=True):
                    addAlphaCoinToStudent(
                        alphaRequest.receiver_id,
                        alphaRequest.amount
                    )
                    transaction.save()
            return Response({"detail":"Transaction Complete"}, status=status.HTTP_201_CREATED)
        return Response({"detail":"Try your transaction again"},status=status.HTTP_408_REQUEST_TIMEOUT)
            
