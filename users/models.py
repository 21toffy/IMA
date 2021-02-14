from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
import datetime as d
# from courses.models import Faculty,Department
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save


def validate_mobile_num(value):
    valid_starters = ['080', '070', '090', '081']
    if len(str(value)) != 11 or [i.isalpha() for i in str(value) if i.isalpha()] :
        raise ValidationError(
            _('%(value)s is not a valid Phone number'),
            params={'value': value},
        )



class UserManager(BaseUserManager):
    def create_user(self, email,firstname,lastname,password=None):
        if not email:
            raise ValueError('you  must input an  email')
        user = self.model(firstname=firstname,lastname=lastname,email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,firstname,lastname,password):
        user = self.create_user(email,firstname,lastname,password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(unique=True, help_text='Please make sure your Email is correct', verbose_name=_("emails"))
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11,validators=[validate_mobile_num], default='+234',help_text='enter in 11 digit format', null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

    class Meta(object):
        unique_together = ('email',)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    REQUIRED_FIELDS = ['firstname','lastname',]