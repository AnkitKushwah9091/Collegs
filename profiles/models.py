from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Collegs Profile"
        verbose_name_plural = "Profiles"
        db_table = "USER_PROFILES"

    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    #User Model --> id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    
    #personal details :-
    birth_date = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=1,blank=True,null=True,choices=GENDERS)
    religion = models.CharField(max_length=30,blank=True,null=True)

    #contact details :-
    contact_no = models.CharField(max_length=15,blank=True,null=True)
    home_town = models.CharField(max_length=100,)
    current_city = models.CharField(max_length=100,blank=True,null=True)

    #verifications details :-
    """ otp = models.CharField(max_length=6, editable=False,blank=True,null=True)
    is_email_verfied = models.BooleanField(default=False)
    is_contact_no_verifed = models.BooleanField(default=False) """

    #profile details :-
    profile_pic = models.ImageField(null=True, blank=True)
    cover_pic = models.ImageField(null=True, blank=True)
    bio = models.TextField(max_length=100, null=True, blank=True,)

    def __str__(self):
        return self.user.username
