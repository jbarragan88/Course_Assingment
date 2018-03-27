from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.

class CourseManager(models.Manager):
    def validate_course(request, postData):
        errors = {}

        #validating Course name 
        if len(postData['name']) < 2 or postData['name'].isalpha():
            if len(postData['name']) < 2:
                errors['name'] = "Course Name must contain more than 2 characters."
            if not postData['name'].isalpha():
                errors['name_alpha'] = "Course Name must contain only characters."

        return errors

class Description(models.Model):
    description = models.CharField(max_length=255)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.OneToOneField(Description)
    creator = models.ForeignKey(User, related_name="created_courses") 
    likers = models.ManyToManyField(User, related_name="liked_courses")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects = CourseManager()

class CommentManager(models.Manager):
    def validate_comment(request, postData):
        errors = {}

        #validating Course name 
        if len(postData['comment']) > 200:
            errors['comment'] = "Comment must contain less than 200 characters."

class Comment(models.Model):
    name = models.ManyToManyField(User, related_name="my_comments")
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="comments")
    likers = models.ManyToManyField(User, related_name="liked_comments")

    objects = CommentManager()