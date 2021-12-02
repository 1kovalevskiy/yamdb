from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

CHOICES = {
    'user': 'user',
    'moderator': 'moderator',
    'admin': 'admin',
}


class User(AbstractUser):
    bio = models.TextField(verbose_name=_('biography'),
                           blank=True)
    email = models.EmailField(verbose_name=_('email address'),
                              unique=True)
    role = models.CharField(verbose_name=_('role'),
                            max_length=20,
                            choices=CHOICES.items(),
                            default=CHOICES['user'],
                            )

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        unique_together = ('email', 'username')

    def __str__(self):
        return self.email

    @property
    def is_moderator(self):
        return self.is_staff or self.role == CHOICES['moderator']

    @property
    def is_admin(self):
        return self.is_superuser or self.role == CHOICES['admin']
