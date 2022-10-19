import datetime
from django.db import models
from students.views import StudentProfessionalDetails
# Create your models here.
class StudentCoinDetail(models.Model): 
     student_professional_detail_id = models.ForeignKey(StudentProfessionalDetails,to_field="bennett_email", on_delete=models.CASCADE)
     alpha_coin=models.PositiveBigIntegerField()
     sigma_coin=models.PositiveBigIntegerField()
     xp=models.PositiveIntegerField()
     level=models.PositiveBigIntegerField()
     current_timestamp=models.DateTimeField(null=True, blank=True, editable=False);
     def save(self, *args, **kwargs):
        self.current_timestamp =datetime.datetime.now()
        super(StudentCoinDetail, self).save(*args, **kwargs)
class FollowRelation(models.Model):
   follower=models.ForeignKey(StudentCoinDetail,to_field="id",on_delete=models.CASCADE,related_name='follower')
   following=models.ForeignKey(StudentCoinDetail,to_field="id",on_delete=models.CASCADE,related_name='following')
   def save(self,*args,**kwargs):
      self.current_timestamp=datetime.datetime.now()
      super(FollowRelation,self).save(args,kwargs)
