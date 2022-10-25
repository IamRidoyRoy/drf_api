# from distutils.command.upload import upload
from django.conf import settings
from django.db import models

# Create a image upload function for create different user folder  
def user_upload_status(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

# Create your models here.

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=user_upload_status, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[0:30]

    # Create a name which will show on django admin 
    class Meta:
        verbose_name_plural = "Status List"