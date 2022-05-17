from django.db.models.signals import post_save, pre_save, post_delete
from django.contrib.auth.models import User
from .models import Account, Person

def create_profile(sender, instance, created, **kwargs):
    if created:
        person = Person.objects.get(iin = instance.username)
        Account.objects.create(
            user = instance,
            person = person
        )
        print('account created')
        
        
post_save.connect(create_profile, sender=User)
