from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
class Note(models.Model):
    user = models.ForeignKey(User, related_name="notes", on_delete=models.DO_NOTHING)
    
    heading = models.CharField(max_length=30)
    body  = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.heading}..."
        )
    
    


#Decides whether to create a new Profile instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        #one-to-one relationship between the user and the profile
        user_profile = Profile(user=instance)
        user_profile.save()


