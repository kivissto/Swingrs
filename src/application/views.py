import pyrebase
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .models import Card

# Firebase Configuration
firebaseConfig = {
    'apiKey': "AIzaSyA8laeG3yxNNJuuzWLli1Aww5_gsEtlVl0",
    'authDomain': "swingrs-django.firebaseapp.com",
    'projectId': "swingrs-django",
    'storageBucket': "swingrs-django.firebasestorage.app",
    'messagingSenderId': "547828218331",
    'appId': "1:547828218331:web:0985eb7d4ac9c64ef44ffe",
    'measurementId': "G-B9PS5T8EZ3",
    # NOTE: you must include the database URL even if unused:
    'databaseURL': "https://swingrs-django-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Views
def landing(request):
    return render(request, 'docking/landing.html')

def createAccount(request):
    return render(request, 'docking/create-account.html')

def forgotPassword(request):
    return render(request, 'docking/forgot-password.html')

def signIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            messages.success(request, f"Welcome back, {email}!")
            return render(request, 'homepage/home.html')

        except Exception as e:
            error_message = str(e)
            messages.error(request, "Invalid email or password.")
            return redirect('landing')

    return render(request, 'docking/landing.html')


def home(request):
    users = []
    try:
        firebase_data = firebase.database().child("Users").get().val()
        print("FIREBASE DATA:", firebase_data)

        if firebase_data:
            for user_id, user in firebase_data.items():
                users.append({
                    "id": user_id,
                    "name": user.get("name", ""),
                    "age": user.get("age", ""),
                    "bio": user.get("bio", ""),
                    "photoUrl": user.get("photoUrl", ""),
                    "gender": user.get("gender", "")
                })
    except Exception as e:
        print("Firebase error:", e)
    return render(request, "homepage/home.html", {"users": users})

def likeCard(request, card_id):
    if request.method == 'POST':
        card = Card.objects.get(id=card_id)
        print(f"Liked: {card.title}")
        return JsonResponse({'status': 'liked'})

def dislikeCard(request, card_id):
    if request.method == 'POST':
        card = Card.objects.get(id=card_id)
        print(f"Disliked: {card.title}")
        return JsonResponse({'status': 'disliked'})

def superlikeCard(request, card_id):
    if request.method == 'POST':
        card = Card.objects.get(id=card_id)
        print(f"Super-liked: {card.title}")
        return JsonResponse({'status': 'disliked'})

def inbox(request):
    users = []
    try:
        firebase_data = firebase.database().child("Users").get().val()
        if firebase_data:
            for user_id, user in firebase_data.items():
                users.append({
                    "id": user_id,
                    "name": user.get("name", ""),
                    "age": user.get("age", ""),
                    "bio": user.get("bio", ""),
                    "photoUrl": user.get("photoUrl", ""),
                    "gender": user.get("gender", "")
                })
    except Exception as e:
        print("Firebase inbox error:", e)
    return render(request, "homepage/inbox.html", {"users": users})

def likes(request):
    return render(request, 'homepage/likes.html')

def venues(request):
    return render(request, 'homepage/venues.html')

def user(request):
    return render(request, 'homepage/user.html')