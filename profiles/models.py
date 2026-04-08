from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    interests = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    def get_interests_list(self):
        return [i.strip().lower() for i in self.interests.split(',') if i.strip()]
