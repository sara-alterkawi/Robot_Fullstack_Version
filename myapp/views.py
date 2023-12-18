from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, OrderHistory
from django.db import IntegrityError
from django.contrib import messages
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse

@login_required(login_url='login')
def HomePage(request):
    if request.method == 'POST':
        id = request.user.id
        user = User.objects.get(username="admin")
        A = request.POST.get('A')
        B = request.POST.get('B')
        C = request.POST.get('C')
        D = request.POST.get('D')
        E = request.POST.get('E')
        F = request.POST.get('F')
        G = request.POST.get('G')
        H = request.POST.get('H')

        history = {}
        history['user'] = request.user
        history['user_name'] = request.user.username

        # return redirect('home')
        if (A):
            count = getattr(user, "A")
            A = int(A)
            if count - A < 0:
                messages.error(request, f"You don't have enough 'A' to complete the order")
                history['error'] = "You don't have enough 'A' to complete the order"
                history['is_error'] = True
                history['A'] = A
                history = OrderHistory(**history)
                return redirect('home')
            history['A'] = A
            setattr(user, "A", count - A)

        if (B):
            count = getattr(user, "B")
            B = int(B)
            if count - B < 0:
                messages.error(request, f"You don't have enough 'B' to complete the order")
                history['error'] = "You don't have enough 'B' to complete the order"
                history['is_error'] = True
                history['B'] = B
                history = OrderHistory(**history)
                return redirect('home')
            history['B'] = B
            setattr(user, "B", count - B)

        if (C):
            count = getattr(user, "C")
            C = int(C)
            if count - C < 0:
                messages.error(request, f"You don't have enough 'C' to complete the order")
                history['error'] = "You don't have enough 'C' to complete the order"
                history['is_error'] = True
                history['C'] = C
                history = OrderHistory(**history)
                return redirect('home')
            history['C'] = C
            setattr(user, "C", count - C)

        if (D):
            count = getattr(user, "D")
            D = int(D)
            if count - D < 0:
                messages.error(request, f"You don't have enough 'D' to complete the order")
                history['error'] = "You don't have enough 'D' to complete the order"
                history['is_error'] = True
                history['D'] = D
                history = OrderHistory(**history)
                return redirect('home')
            history['D'] = D
            setattr(user, "D", count - D)
        
        if (E):
            count = getattr(user, "E")
            E = int(E)
            if count - E < 0:
                messages.error(request, f"You don't have enough 'E' to complete the order")
                history['error'] = "You don't have enough 'E' to complete the order"
                history['is_error'] = True
                history['E'] = E
                history = OrderHistory(**history)
                return redirect('home')
            history['E'] = E
            setattr(user, "E", count - E)

        if (F):
            count = getattr(user, "F")
            F = int(F)
            if count - F < 0:
                messages.error(request, f"You don't have enough 'F' to complete the order")
                history['error'] = "You don't have enough 'F' to complete the order"
                history['is_error'] = True
                history['F'] = F
                history = OrderHistory(**history)
                return redirect('home')
            history['F'] = F
            setattr(user, "F", count - F)

        if (G):
            count = getattr(user, "G")
            G = int(G)
            if count - G < 0:
                messages.error(request, f"You don't have enough 'G' to complete the order")
                history['error'] = "You don't have enough 'G' to complete the order"
                history['is_error'] = True
                history['G'] = G
                history = OrderHistory(**history)
                return redirect('home')
            history['G'] = G
            setattr(user, "G", count - G)

        if (H):
            count = getattr(user, "H")
            H = int(H)
            if count - H < 0:
                messages.error(request, f"You don't have enough 'H' to complete the order")
                history['error'] = "You don't have enough 'H' to complete the order"
                history['is_error'] = True
                history['H'] = H
                history = OrderHistory(**history)
                return redirect('home')
            history['H'] = H
            setattr(user, "H", count - H)

        # Update the user record
        user.save()

        history = OrderHistory(**history)
        history.save()

        channel_layer = get_channel_layer()

        # Define the message you want to send
        test_message = "This is a test message from the HTTP view!"

        # Send the message to the "raspberry_pi_group" WebSocket group
        async_to_sync(channel_layer.group_send)(
            "raspberry_pi",
            {
                "type": "raspberry_pi.message",
                "message": {
                "A": A,
                "B": B,
                "C": C,
                "D": D,
                "E": E,
                "F": F,
                "G": G,
                "H": H
                }
            }
        )
        messages.success(request, "Order successfully placed.")
        return redirect('home')

    return render(request, 'home.html')

def Signup(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')

        if password_1 != password_2:
            messages.error(request, "Your password and confirmation password do not match.")
            return redirect('signup')

        try:
            user = User.objects.create_user(username=email, password=password_1)
            user.save()
        except IntegrityError as e:
            messages.error(request, "Username (email) is already in use.")
            return redirect('signup')
        try:
            user = User.objects.create_user(username="admin", password="admin")
            user.save()
        except IntegrityError as e:
            pass

        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')

    return render (request,'signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!!!")
            return redirect('login')

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('login')

def AboutPage(request):
    return render(request, 'about.html')

def OrderPage(request):
    orders = OrderHistory.objects.filter(user=request.user).order_by('-date')
    return render(request, 'order.html', {'orders': orders})

def RasPi(request):
    return render(request, "raspi.html")