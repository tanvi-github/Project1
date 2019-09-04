from django.db import models

# Create your models here.
class Document1(models.Model):
    description=models.CharField(max_length=255,blank=True)
    document=models.FileField(upload_to='Images/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.description+" "+self.document

# MODEL TO SAVE DETAILS ....FOR TRAINER REGISTRATION
class tb_TrainerRegistration(models.Model):
    Name = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Employee_ID = models.CharField(max_length=200)
    Email_ID = models.CharField(max_length=200)
    Contact = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

#MODEL TO SAVE DETAILS....FOR ADD BATCH
class tb_Registration(models.Model):
    technology=models.CharField(max_length=225)
    trainer_name = models.CharField(max_length=225)
    lab_assign = models.CharField(max_length=225)
    batch_type = models.CharField(max_length=10)
    batch_status = models.CharField(max_length=15)
    batch_code = models.CharField(max_length=10)

