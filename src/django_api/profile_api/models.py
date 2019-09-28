from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""
    

    # this function tells django how to create a user using our custom user model
    def create_user(self, email, name, password=None):
        """creates a new user profile object"""
    
        if not email:
            raise ValueError('Users must have an email address.')

        # normalising the email i.e, it converts all the email address to lowercase
        email = self.normalize_email(email)

        # after normalizing the email, create a new user model
        user = self.model(email=email, name=name)

        # and then set the password, the set_password functions encrypts the password before sending it to the database
        user.set_password(password)
        user.save(using=self.db)

        # finally, return the user
        return user

        # the next function is used to tell django how to create a super user
        def create_superuser(self, email, name, password):
            """creates and saves a new superuser with given details"""

            user = self.create_user(email, name, password)

            user.is_superuser = True
            user.is_staff = True

            user.save(using=self.db)

            return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """This class represents a user's profile in our model"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    # set an object manager that will help us manage the user profile
    objects = UserProfileManager()

    # overide the default username field to allow users login with their email
    USERNAME_FIELD = 'email'
    
    # these are the required fields for all user objects in the system
    REQUIRED_FIELDS = ['name']

    # next, we will create helper functions
    def get_full_name(self):
        """This is used to get a user's full name"""

        return self.name

    def get_short_name(self):
        """use to get a user's shprtname"""

        return self.name

    def  __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email