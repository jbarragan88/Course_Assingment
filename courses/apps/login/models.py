from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(models.Manager):
    def validate_user(request, postData):
        errors = {}

        #validating first name 
        if len(postData['first_name']) < 2 or postData['first_name'].isalpha():
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First Name must contain more than 2 characters."
            if not postData['first_name'].isalpha():
                errors['first_name_alpha'] = "First Name must contain only characters."

        #validating last name 
        if len(postData['last_name']) < 2 or postData['last_name'].isalpha():
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last Name must contain more than 2 characters."
            if not postData['last_name'].isalpha():
                errors['last_name_alpha'] = "Last Name must contain only characters."

        #validating email
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "This is not a valid email."
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists."

        #validating password
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if postData['password'] != postData['cpassword']:
            errors['cpassword'] = "Passwords must match"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password =  models.CharField(max_length=255)

    objects = UserManager()