from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import account,yellowitem,roseitem,blueitem,whiteitem,specialkit,complaints,compaction,application,replays,client,register_table
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from fps1.settings import EMAIL_HOST_USER

# Create your views here.
@login_required
def home(request):
	return render(request,'addaccount.html')

def adminheader1(request):
    return render(request,"adminheader.html")



def addacct1(request):
	responseDic={}
	try:
			actlist=account()
			act_id=request.POST['act_id']
			rashop_id=request.POST['rashop_id']
			place=request.POST['place']
			phone=request.POST['phone']
			email=request.POST['email']
			actlist=account(act_id=act_id,rashop_id=rashop_id,place=place,phone=phone,email=email)
			actlist.save()
			responseDic["msg1"]="Account added"
			return render(request,"addaccount.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Account cannot be added"
		return render(request,"addaccount.html",responseDic)

def removeact1(request):
	try:
		place=request.POST['place']
		phone=request.POST['phone']
		actlist=account.objects.filter(place=place,phone=phone)
		actlist.delete()
		return render(request,"removeaccount.html",{'msg3':"Deleted"})
	except Exception as e:
		return render(request,"removeaccount.html",{'msg3':"Can not be Deleted"})

def updtact1(request):
	try:
		phone=request.POST['num']
		newnum=request.POST['newnum']
		actlist=account.objects.get(id=3)
		actlist.phone=newnum
		actlist.save()
		
		return render(request,"updtact.html",{'msg2':newnum +" "+"updated"})
	except Exception as e:
		return render(request,"updtact.html",{'msg2':"Can not be updated"})


def rationshopheader1(request):
    return render(request,"rationshopheader.html")


def addyitems1(request):
	responseDic={}
	try:
		yitem_id=request.POST['yitem_id']
		yitem=request.POST['yitem']
		yquantity=request.POST['yquantity']
		yitlist=yellowitem(yitem_id=yitem_id,yitem=yitem,yquantity=yquantity)
		yitlist.save()
		responseDic["msg1"]="Item added"
		return render(request,"addyitems.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Item cannot be added"
		return render(request,"addyitems.html",responseDic)

def addritems1(request):
	responseDic={}
	try:
		ritem_id=request.POST['ritem_id']
		ritem=request.POST['ritem']
		rquantity=request.POST['rquantity']
		ritlist=roseitem(ritem_id=ritem_id,ritem=ritem,rquantity=rquantity)
		ritlist.save()
		responseDic["msg1"]="Item added"
		return render(request,"addritems.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Item cannot be added"
		return render(request,"addritems.html",responseDic)

def addbitems1(request):
	responseDic={}
	try:
		bitem_id=request.POST['bitem_id']
		bitem=request.POST['bitem']
		bquantity=request.POST['bquantity']
		bitlist=blueitem(bitem_id=bitem_id,bitem=bitem,bquantity=bquantity)
		bitlist.save()
		responseDic["msg1"]="Item added"
		return render(request,"addbitems.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Item cannot be added"
		return render(request,"addbitems.html",responseDic)

def addwitems1(request):
	responseDic={}
	try:
		witem_id=request.POST['witem_id']
		witem=request.POST['witem']
		wquantity=request.POST['wquantity']
		witlist=whiteitem(witem_id=witem_id,witem=witem,wquantity=wquantity)
		witlist.save()
		responseDic["msg1"]="Item added"
		return render(request,"addwitems.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Item cannot be added"
		return render(request,"addwitems.html",responseDic)

def addkititems1(request):
	responseDic={}
	try:
		spkit_id=request.POST['spkit_id']
		apkitem=request.POST['apkitem']
		spkquantity=request.POST['spkquantity']
		spklist=specialkit(spkit_id=spkit_id,apkitem=apkitem,spkquantity=spkquantity)
		spklist.save()
		responseDic["msg1"]="Item added"
		return render(request,"addspclkit.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Item cannot be added"
		return render(request,"addspclkit.html",responseDic)

def removespclkit1(request):
	try:
		apkitem=request.POST['apkitem']
		spkquantity=request.POST['spkquantity']
		spklist=specialkit.objects.filter(apkitem=apkitem,spkquantity=spkquantity)
		spklist.delete()
		return render(request,"removespclkit.html",{'msg3':"Deleted"})
	except Exception as e:
		return render(request,"removespclkit.html",{'msg3':"Can not be Deleted"})

def customerheader1(request):
    return render(request,"customerheader.html")

def yitemdis1(request):
	yitlist=yellowitem.objects.all()
	return render(request,"yitemdis.html",{'yit':yitlist})

def ritemdis1(request):
	ritlist=roseitem.objects.all()
	return render(request,"ritemdis.html",{'rit':ritlist})

def bitemdis1(request):
	bitlist=blueitem.objects.all()
	return render(request,"bitemdis.html",{'bit':bitlist})

def witemdis1(request):
	witlist=whiteitem.objects.all()
	return render(request,"witemdis.html",{'wit':witlist})
		
def spclkititdis1(request):
	spklist=specialkit.objects.all()
	return render(request,"specialkitdis.html",{'spit':spklist})

def custcomplaint1(request):
	responseDic={}
	try:
		complaint_id=request.POST['complaint_id']
		customer_id=request.POST['customer_id']
		complaint=request.POST['complaint']
		complaint_date=request.POST['complaint_date']
		place=request.POST['place']
		contact=request.POST['contact']
		complist=complaints(complaint_id=complaint_id,customer_id=customer_id,complaint=complaint,complaint_date=complaint_date,place=place,contact=contact)
		complist.save()
		responseDic["msg1"]="complaint Registerd"
		return render(request,"custcomplaint.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="complaint cannot be Registerd"
		return render(request,"custcomplaint.html",responseDic)
		
def verifycomp1(request):
	complist=complaints.objects.all()
	return render(request,"verifycomplaint.html",{'vcomp':complist})		

def take_action1(request):
	responseDic={}
	try:
		action_id=request.POST['action_id']
		complaint_id=request.POST['complaint_id']
		action=request.POST['action']
		action_date=request.POST['action_date']
		redirect_to=request.POST['redirect_to']
		actlist=compaction(action_id=action_id,complaint_id=complaint_id,action=action,action_date=action_date,redirect_to=redirect_to)
		actlist.save()
		responseDic["msg1"]="Action proceed"
		return render(request,"takeaction.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Action cannot be Proceed"
		return render(request,"takeaction.html",responseDic)

def viewacct1(request):
	actlist=account.objects.all()
	return render(request,"viewaccount.html",{'viact':actlist})

def viewcompaction1(request):
	actlist=compaction.objects.all()
	return render(request,"viewcompaction.html",{'vcmpact':actlist})

def newapplication1(request):
	responseDic={}
	try:
		application_id=request.POST['application_id']
		name=request.POST['name']
		age=request.POST['age']
		gender=request.POST['gender']
		address=request.POST['address']
		contact=request.POST['contact']
		members_count=request.POST['members_count']
		anual_income=request.POST['anual_income']
		email=request.POST['email']
		applist=application(application_id=application_id,name=name,age=age,gender=gender,address=address,contact=contact,members_count=members_count,anual_income=anual_income,email=email)
		applist.save()
		responseDic["msg1"]="Request Registerd"
		return render(request,"newapplication.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Request cannot be registerd"
		return render(request,"newapplication.html",responseDic)
		
def viewappreq1(request):
	applist=application.objects.all()
	return render(request,"viewapplicationrq.html",{'aprq':applist})

def rqstreplay1(request):
	responseDic={}
	try:
		replay=request.POST['replay']
		rplist=replays(replay=replay)
		rplist.save()
		responseDic["msg1"]="Replay send"
		return render(request,"rqstreply.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Replay cannot be send"
		return render(request,"rqstreply.html",responseDic)

def viewrqstreplay1(request):
	rplist=replays.objects.all()
	return render(request,"viewapprqst.html",{'aprqrp':rplist})

def publicheader1(request):
    return render(request,"publicheader.html")

def registerclient1(request):
	responseDic={}
	try:
		customer_id=request.POST['customer_id']
		src_no=request.POST['src_no']
		name=request.POST['name']
		age=request.POST['age']
		address=request.POST['address']
		total_members=request.POST['total_members']
		contact=request.POST['contact']
		email=request.POST['email']
		cllist=client(customer_id=customer_id,src_no=src_no,name=name,age=age,address=address,total_members=total_members,contact=contact,email=email)
		cllist.save()
		responseDic["msg1"]="Client Registerd successfully"
		return render(request,"registerclient.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Client cannot be registerd"
		return render(request,"registerclient.html",responseDic)		



def admin1(request):
	return render(request,"admin.html")

def ration1(request):
	return render(request,"rationshop.html")

def customer1(request):
	return render(request,"customer.html")

def viewmem1(request):
	cllist=client.objects.all()
	return render(request,"viewmemb.html",{'mem':cllist})

def viewcomp1(request):
	complist=complaints.objects.all()
	return render(request,"viewcomplaint.html",{'cmp':complist})

def viewmembers1(request):
	cllist=client.objects.all()
	return render(request,"viewmembers.html",{'memb':cllist})

def index(request):
	return render(request,"index.html")

def doc1(request):
	return render(request,"doc.html")

def register(request):
	if request.method=="POST":
		fname=request.POST["first_name"]
		last=request.POST["last_name"]
		un=request.POST["username"]
		em=request.POST["email"]
		phn=request.POST["phn_number"]
		pwd=request.POST["psw"]
		rpwd=request.POST["psw-repeat"]
		tp=request.POST["utype"]

		usr=User.objects.create_user(username=un,email=em,password=pwd)
		usr.first_name=fname
		usr.last_name=last
		if tp=="employee":
			usr.is_customer=True
		usr.save()
		reg=register_table(user=usr,phone_number=phn)
		reg.save()
		return render(request,"registration/login.html",{"status":"{} Register Successfully".format(fname)})

	return render(request,"registration.html")



def user_login(request):
	if request.method=="POST":
		un=request.POST["username"]
		ps=request.POST["password"]
		
		user=authenticate(username=un,password=ps)
		if user:
			login(request,user)
			if user.is_admin: 
				return redirect("admin1")
			if user.is_customer:
				return redirect("ration1")
			if user.is_customer:
				return redirect("customer1")
	else:
		return render(request,'user_login.html',{"status":"Invalid User Name or Password"})

def logout_view(request):
	logout(request)
	return redirect('login')

def Resethome(request):
	return render(request,'registration/ResetPassword.html')


def resetPassword(request):
	responseDic={}
	try:
		username=request.POST['uname']
		recepient=request.POST['email']
		pwd=request.POST['password']
		subject="Password reset"
		try:
			user=User.objects.get(username=username)
			if user is not None:
				user.set_password(pwd)
				user.save()
				message="Your Password Was Changed"
				send_mail(subject,message, EMAIL_HOST_USER, [recepient])
				responseDic["errmsg"]="Password Reset Successfully"
				return render(request,"registration/ResetPassword.html",responseDic)
		except Exception as e:
			print(e)
			responseDic["errmsg"]="Email doesnot exist"
			return render(request,"registration/ResetPassword.html",responseDic)
	except Exception as e:
			print(e)
			responseDic["errmsg"]="Failed to reset password"
			return render(request,"registration/ResetPassword.html",responseDic)







