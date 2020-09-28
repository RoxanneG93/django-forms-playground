from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from user.models import User

# Create your models here.

# I want a Bidirectional relationship based on User and Quizes
# Want to be able to look up the Quizes User has completed from User
# We are going to be storing many QuizA instances filled out from different Users
# So we need to have QuizA data stored with UserId


# class FormsProgress(models.Model)


# Parent class that whole forms will inherit from 
class BaseForm(models.Model):
    date_completed = models.DateTimeField(null=True)
    date_started = models.DateTimeField(null=True)
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=100)


# Form that requires info from User for thier address and medication
class QuestionaireA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    # demographics_section = ForeignKey()

    def __str__(self):
        return self.title


# These will be Json models containing the questions and ansers in key value pairs
class DemographicsSection(models.Model):
    title = models.CharField(max_length=100)
    address_content = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# These will be Json models containing the questions and ansers in key value pairs
class MedicationsSection(models.Model):
    medication_content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

# class UserProfile(models.Model):
#     # There could be a seperate table for pending quizes that need to be completedd
#     completed_forms = 
#     started_forms = 


