from django.db import models
from uuid import uuid4
from authemail.models import EmailUserManager, EmailAbstractUser

class MyUser(EmailAbstractUser):
	# Required
	objects = EmailUserManager()
	seller_id = models.UUIDField(default=uuid4, unique=True)