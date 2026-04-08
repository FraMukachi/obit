from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from django.contrib.auth import get_user_model
from currency.models import OrbitWallet

User = get_user_model()

@login_required
@csrf_exempt
def chat_view(request, user_id):
    other_user = User.objects.get(id=user_id)
    
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    )
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                sender=request.user,
                receiver=other_user,
                content=content
            )
            # Earn 1 Orbit for sending a message
            wallet, _ = OrbitWallet.objects.get_or_create(user=request.user)
            wallet.balance += 1
            wallet.save()
        return redirect('chat', user_id=user_id)
    
    return render(request, 'chat.html', {
        'other_user': other_user,
        'messages': messages
    })
