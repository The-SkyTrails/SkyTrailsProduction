# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from django_countries.fields import CountryField

# DEPARTMENT_CHOICES = (
#     ('Documentation','Documentation'),
#     ('Sales','Sales'),
#     ('Account','Account'),
#     ('HR','HR'),
#     ('Admin','Admin')
# )

# STATUS_CHOICES = (
#         ('1', 'Active'),
#         ('0', 'Inactive'),
#     )

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default="Department Name")
#     contact_number = models.CharField(max_length=15, unique=True)
#     country = CountryField(blank_label='(select country)')
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     address = models.TextField()
#     zipcode = models.CharField(max_length=20)
#     status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
#     photo = models.ImageField(upload_to="Images/user/")
    
    
#     def __str__(self):
#          return f"{self.first_name} {self.last_name}"
     
     