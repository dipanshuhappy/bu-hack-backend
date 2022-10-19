from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from students.models import StudentProfessionalDetails
from staffs.models import StaffProfessionalDetails
from rest_framework import generics
from .serializer import RegisterSerializer
from django.contrib.auth.models import User


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,_= Token.objects.get_or_create(user=user)
        user_type =request.data['type']
        print("user==>",user)
        if(user_type=="student"):
            student_id = StudentProfessionalDetails.objects.get(enrollment_number=user).id
            return Response({
            'token': token.key,
            'user_id': user.pk,
            'student_id':student_id 
            })
        elif (user_type=="staff"):
            staff_id = StaffProfessionalDetails.objects.get(bennett_email=str(user)+"@bennett.edu.in").id
            return Response({
                'token':token.key,
                'user_id':user.pk,
                'staff_id':staff_id
            })
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer