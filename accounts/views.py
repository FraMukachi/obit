from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from .models import User
from currency.models import OrbitWallet

def landing_page(request):
    return render(request, 'landing.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Create user (not verified yet)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_verified = False
        user.email_verification_token = get_random_string(50)
        user.save()
        
        # Create wallet with bonus
        OrbitWallet.objects.create(user=user, balance=50)
        
        # Send verification email
        verification_link = f"https://obit.onrender.com/verify/{user.email_verification_token}/"
        send_mail(
            'Verify your Orbit account',
            f'Click this link to verify your account: {verification_link}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=True,
        )
        
        login(request, user)
        return redirect('verify_pending')
    return render(request, 'signup.html')

def verify_pending(request):
    return render(request, 'verify_pending.html')

def verify_email(request, token):
    try:
        user = User.objects.get(email_verification_token=token)
        user.is_verified = True
        user.email_verification_token = ''
        user.save()
        return redirect('dashboard')
    except User.DoesNotExist:
        return redirect('signup')

@login_required
def dashboard(request):
    wallet, created = OrbitWallet.objects.get_or_create(user=request.user)
    claimed = wallet.claim_daily()
    
    return render(request, 'dashboard.html', {
        'user': request.user,
        'wallet': wallet,
        'claimed_today': claimed,
    })

@csrf_exempt
def custom_logout(request):
    logout(request)
    return redirect('/')
