from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    # Add any additional attributes you want
    mobile_no = models.IntegerField()

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username.IntegerField(blank=True)