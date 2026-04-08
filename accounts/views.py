from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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
        user = User.objects.create_user(username=username, email=email, password=password)
        # Create wallet for new user with 50 bonus Orbits
        wallet = OrbitWallet.objects.create(user=user, balance=50)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'signup.html')

@login_required
def dashboard(request):
    # Get or create wallet
    wallet, created = OrbitWallet.objects.get_or_create(user=request.user)
    
    # Claim daily bonus automatically
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
