from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# all media of post will be stored in this model like images, videos, audio, document etc
class OfficerProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="officer", blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='officer_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    usergroup = models.CharField(default="officer", max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    profile_is_completed = models.BooleanField(default=False)
    physical_address = models.CharField(max_length=50000, blank=True, null=True)

    @property
    def get_image(self):
        if self.image:
            return self.image.url
        return None

    @property
    def phone_number(self):
        return self.user.phone_number
    
    @property
    def get_user_id(self):
        return self.user.id
    
    # def __str__(self):
    #     return self.name
    