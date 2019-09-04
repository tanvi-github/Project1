from django import forms
from .models import Document1


class DocumentForm(forms.ModelForm): #link model in form
    class Meta: #inner class
        model = Document1
        fields=('description','document')


#For practice/TRy

"""
FRUIT_CHOICES = [
        ('orange', 'Oranges'),
        ('cantaloupe', 'Cantaloupes'),
    ]
       class UserForm(forms.Form):
        first_name = forms.CharField(max_length=100)
        last_name = forms.CharField(max_length=100)
        email = forms.EmailField()
        age = forms.IntegerField()
        favorite_fruit = forms.CharField(label='What is your favorite fruit?',
                                         widget=forms.Select(choices=FRUIT_CHOICES))"""

lang = [
    ('select an option', 'select an option '),
    ('Python', 'Python'),
    ('C', 'C'),
    ('Java', 'Java'),
]
teacher = [
    ('select an option ', 'select an option '),
    ('Sipika', 'Sipika'),
    ('Shikhi', 'Shikhi'),
    ('Shruti', 'Shruti'),
    ('Shweta','Shweta'),
]
room = [
    ('select an option ', 'select an option '),
    ('Vidya', 'Vidya'),
    ('Gyan', 'Gyan'),
    ('Lakshya', 'Lakshya'),
    ('Vigyan','Vigyan'),
    ('Shiksha','Shiksha'),
    ('Aadhar','Aadhar'),
]
duration = [
    ('select an option ', ' select an option'),
    ('3M-R', '3M-R'),
    ('IT-6M', 'IT-6M'),
    ('IT-6W / IT-4W', 'IT-6W / IT-4W'),
    ('1M-SEL','1M-SEL'),
    ('1 YR','1 YR'),
    ('2 YRS','2 YRS'),
    ('2M-R','2M-R'),
    ('R-6M','R-6M'),
]
state = [
    (' select an option', ' select an option'),
    ('process', 'process'),
    ('complete', 'complete'),
]
"""code = [
    ('select an option ', ' select an option'),
    ('0603', '0603'),
    ('0303', '0303'),
      ]"""

class RegistrationForm(forms.Form):
 technology = forms.CharField(label='Technology',widget=forms.Select(choices=lang))
 trainer_name = forms.CharField(label='trainer name', widget=forms.Select(choices=teacher))
 lab_assign = forms.CharField(label='lab_assign', widget=forms.Select(choices=room))
 batch_type = forms.CharField(label='batch_type', widget=forms.Select(choices=duration))
 batch_status=forms.CharField(label='batch_status',widget=forms.Select(choices=state))
 batch_code=forms.CharField(label='enter batch code',max_length=10)

# Form For Trainer Registration
class TrainerRegForm(forms.Form):
     Name = forms.CharField(label="Name ", required=True, max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your name here'}))
     Choices = [('Female', 'Female'), ('Male', 'Male')]
     Gender = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
     Employee_ID = forms.CharField(label="Employee ID ", required=True, max_length=200,
                                   widget=forms.TextInput(attrs={'placeholder': 'Enter unique employee ID'}))
     Email_ID = forms.CharField(label="Email ID ", required=True, max_length=200,
                                widget=forms.EmailInput(attrs={'placeholder': 'Enter your email ID'}))
     Contact = forms.CharField(label="Contact number ", required=True, max_length=200,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your contact number'}))
     Password = forms.CharField(label="Enter password ", required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
     Password1 = forms.CharField(label="Confirm password ", required=True,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'Confirm spassword'}))

# Form For Trainer Login
class TrainerLogin(forms.Form):
     Employee_ID = forms.CharField(label="Employee ID ", required=True, max_length=200,
                                   widget=forms.TextInput(attrs={'placeholder': 'Enter unique employee ID'}))
     Password = forms.CharField(label="Enter password ", required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

