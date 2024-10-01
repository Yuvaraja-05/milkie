from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .services.razorpay_service import create_order, verify_payment
from .models import Payment 



def index(request):
    buy=Buys.objects.all()
    return render(request,'base.html')

    
def final(request):
    return render(request,'buy.html')

def signup(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        mail=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['cpassword']
        user=User.objects.create_user(username=user_name,first_name=first_name, last_name= last_name,email=mail,password=password1)
        user.save()
        send_mail(
            'Thank you for Signup',#sub
            'welcome to Milkie Dairy products',#msg
            'yuvin3969@gmail.com',#from
            [mail],#to
            fail_silently=False
        )
        print("user created")
        return redirect('/')
    else:
        return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(requests,'invalid credential')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def milk(request):
    return render(request,'milk.html')
def curd(request):
    return render(request,'curd.html')
def butter(request):
    return render(request,'butter.html')

def cheese(request):
    return render(request,'cheese.html')
def buttermilk(request):
    return render(request,'buttermilk.html')
def ghee(request):
    return render(request,'ghee.html')
def condensed(request):
    return render(request,'condensed.html')
def yogurt(request):
    return render(request,'yogurt.html')

def initiate_payment(request):
    
    if request.method == "POST":
        a=request.POST['name']
        b=request.POST['product']
        c=request.POST['quantity']
        d=request.POST['address']
        e=request.POST['phone']
        f=request.POST['email']
        buy=Buys(name=a,product=b,quantity=c,address=d,phone=e,email=f)
        buy.save()
        amount_str = request.POST.get('amount', '').strip()  # Get amount and remove any whitespace
        if not amount_str or not amount_str.isdigit():  # Check if amount is missing or not a valid number
            return render(request, 'payments/pay.html', {
                'error': 'Please enter a valid amount.'
            })
        
        amount = int(amount_str)  # Convert to int only after validation

        order = create_order(amount)  # Create Razorpay order
        context = {
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'order_id': order['id'],
            'amount': amount * 100,  # Convert to paise for Razorpay
            'currency': order['currency'],
        }
        return render(request, 'payments/checkout.html', context)

    return render(request, 'payments/pay.html')

       

@csrf_exempt
def payment_callback(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')
        amount_in_paise = request.POST.get('amount')  # Amount is in paise

        if verify_payment(payment_id, order_id, signature):
            amount_in_rupees = int(amount_in_paise) / 100  # Convert paise to rupees before saving
            Payment.objects.create(
                payment_id=payment_id,
                order_id=order_id,
                amount=amount_in_rupees,  # Save the amount in rupees
                status='Success'
            )
            return render(request, 'payments/success.html')
        else:
            amount_in_rupees = int(amount_in_paise) / 100  # Convert paise to rupees
            Payment.objects.create(
                payment_id=payment_id,
                order_id=order_id,
                amount=amount_in_rupees,  # Save the amount in rupees
                status='Failed'
            )
            return render(request, 'payments/failure.html')
    return redirect('initiate_payment')
