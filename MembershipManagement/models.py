from django.db import models
from django.conf import settings
from CommonApp.choices import MEMBERSHIP_CHOICES, SUBS_PLAN_CHOICES

class Membership(models.Model):
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, default="Free",
        max_length=30
    )

def __str__(self):
    return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="user_membership", on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, related_name="user_membership", on_delete=models.SET_NULL, null=True)

    def __str__(self):
       return self.user.username


class SubscriptionPlans(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name="subscription", on_delete=models.CASCADE)
    subscription_plans_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, default="Free",
        max_length=30
    )
    date_joined = models.DateTimeField(verbose_name='date paid', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='end of current plan', auto_now=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
          return self.user_membership.user.username
