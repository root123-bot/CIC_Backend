from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class MkulimaProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="mkulima", blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mkulima_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usergroup = models.CharField(default="mkulima", max_length=50)
    is_active = models.BooleanField(default=True)

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
    
    def __str__(self):
        return self.name
    