# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

class UserManager(models.Manager):
    def checkfirst(self, request, post_data):
        #validation of length field
        if len(post_data['first_name']) < 3 or len(post_data['last_name']) < 3 or len(post_data['email']) < 3:
            messages.error(request, 'You Need More Than Three Letters')
        if len(self.filter(email=request.POST['email'])) > 0:
            messages.error(request, 'email needs to be unique')
        else:
            newuser = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email']


            )

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add = True)
   # updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email

    def fullname(self):
        users = User.objects.all()
        return "{} {}".format(self.first_name , self.last_name)

    def emailaddress(self):
        return "{}".format(self.email)






# Create your models here.
