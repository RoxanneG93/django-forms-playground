from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, is_staff=True, is_admin=False, is_active=False): # if full name was required you would add it to paremeters here
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must provide a password")
        user = self.model(
            email = self.normalize_email(email)
        )
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.set_password(password) # built in method, you would use this method to change the password as well
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        user.save(using=self._db)
        return user


#This AbtractBaseUser already comes with id, password, and last_login fields by default
# In this example our User Model will be Unique Email centeric - not by username
class User(AbstractBaseUser):
    # username = models.Charfiled()  - you can make your own username field override
    email = models.EmailField(unique=True, max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True) # can login
    staff = models.BooleanField(default=False) # staff user non superuser
    admin = models.BooleanField(default=False) # superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email' # this would be 'username if you were doing a custom username field
    # USERNAME_FIELD  and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] # the py createsuperuser command will ask these required fields

    objects = UserManager()

    def _str_(self):
        return self.email

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    #these methods will make it easier to get results
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active


# You may want to create a seperate app for Profiles
# Will contain the user's info address, phone number, etc
# class Profile(models.Model):
#     user = models.OneToOneField(User)
    # extend extra data