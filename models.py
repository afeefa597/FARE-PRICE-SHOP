
from django.db import models
from django.contrib.auth.models import User,auth


# Create your models here.
class account(models.Model):
	act_id=models.CharField(max_length=20)
	rashop_id=models.CharField(max_length=20)
	place=models.CharField(max_length=20)
	phone=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	
class yellowitem(models.Model):
	yitem_id=models.CharField(max_length=20)
	yitem=models.CharField(max_length=20)
	yquantity=models.CharField(max_length=20)

class roseitem(models.Model):
	ritem_id=models.CharField(max_length=20)
	ritem=models.CharField(max_length=20)
	rquantity=models.CharField(max_length=20)

class blueitem(models.Model):
	bitem_id=models.CharField(max_length=20)
	bitem=models.CharField(max_length=20)
	bquantity=models.CharField(max_length=20)

class whiteitem(models.Model):
	witem_id=models.CharField(max_length=20)
	witem=models.CharField(max_length=20)
	wquantity=models.CharField(max_length=20)

class specialkit(models.Model):
	spkit_id=models.CharField(max_length=20)
	apkitem=models.CharField(max_length=20)
	spkquantity=models.CharField(max_length=20)

class complaints(models.Model):
	complaint_id=models.CharField(max_length=20)
	customer_id=models.CharField(max_length=20)
	complaint=models.CharField(max_length=250)
	complaint_date=models.CharField(max_length=20)
	place=models.CharField(max_length=20)
	contact=models.CharField(max_length=20)

class compaction(models.Model):
	action_id=models.CharField(max_length=20)
	complaint_id=models.CharField(max_length=20)
	action=models.CharField(max_length=250)
	action_date=models.CharField(max_length=20)
	redirect_to=models.CharField(max_length=20)

class application(models.Model):
	application_id=models.CharField(max_length=20)
	name=models.CharField(max_length=20)
	age=models.CharField(max_length=20)
	gender=models.CharField(max_length=20)
	address=models.CharField(max_length=20)
	contact=models.CharField(max_length=20)
	members_count=models.CharField(max_length=20)
	anual_income=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
class replays(models.Model):
	replay=models.CharField(max_length=90)

class client(models.Model):
	customer_id=models.CharField(max_length=20)
	src_no=models.CharField(max_length=20)
	name=models.CharField(max_length=20)
	age=models.CharField(max_length=20)
	address=models.CharField(max_length=20)
	total_members=models.CharField(max_length=20)
	contact=models.CharField(max_length=20)
	email=models.CharField(max_length=20)

class register_table(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)

	phone_number=models.CharField(max_length=12)

	def _str_(self):
		return self.user.username