from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from main.models import Bet

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logoutUser(request):
    logout(request)
    return redirect('loginUser')

@login_required
def fetchUser(request, user_id):

    user = get_object_or_404(User, id=user_id)
    user_bets = Bet.objects.filter(user=user)

    return render(request, 'user.html', {'user_bets':user_bets})