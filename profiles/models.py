from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    """
    Customized Profile model which:
    Define constants for user status choices,
    Define choices for the user status field
    """
    USER_STATUS_BASIC = 'basic'
    USER_STATUS_APPRENTICE = 'apprentice'
    USER_STATUS_EXPERIENCED = 'experienced'
    USER_STATUS_MASTER = 'master'

    USER_STATUS_LEVELS = [
        (USER_STATUS_BASIC, 'basic'),
        (USER_STATUS_APPRENTICE, 'apprentice'),
        (USER_STATUS_EXPERIENCED, 'experienced'),
        (USER_STATUS_MASTER, 'master'),
    ]

    user_status = models.CharField(
        max_length=20,
        choices=USER_STATUS_LEVELS,
        default=USER_STATUS_BASIC,
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    nickname = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    member_since = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/',
    )

    @property
    def email(self):
        return self.owner.email

    @property
    def username(self):
        return self.owner.username

    class Meta:
        ordering = ['-member_since']

    def __str__(self):
        return f"{self.owner}'s profile"

    def save(self, *args, **kwargs):
        """
        Custom save method that sets the profile picture based on
        user status
        """
        if self.user_status == self.USER_STATUS_APPRENTICE:
            self.image = '../apprentice_vcpdlr'
        elif self.user_status == self.USER_STATUS_EXPERIENCED:
            self.image = '../experienced_vmfnxw'
        elif self.user_status == self.USER_STATUS_MASTER:
            self.image = '../master_ebljsl'
        else:
            self.image = '../default_profile_cci3e7'
        super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Links to post_save and signals Profile creation
    when User is created
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
