from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

class MyUser(EmailAbstractUser):
	# Required
	objects = EmailUserManager()
	address = models.TextField(max_length = 500, blank = True, default = '')
	phone = models.CharField(max_length = 10, blank = True, default = '0000000000')
	def update_Address(self, address):
		self.address = address
	def update_phone(self, phone):
		self.phone = phone
		