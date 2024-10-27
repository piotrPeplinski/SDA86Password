import random
from django.shortcuts import render
import string
# tworzenie, aktywacja, dezaktywacja env
# tworzenie projektu
# tworzenie aplikacji (co to jest, po co to jest)
# uruchamianie serwera
# flow danych
# django template language (DTL)

# Create your views here.


def home(request):
    return render(request, 'home.html')


def creator(request):
    return render(request, 'creator.html')


def password_form(request):
    return render(request, 'password_form.html')

# wygenerowac haslo, takie jak poprosil uzytkownik
# wyswietlic je w templatce
# haslo tylko z malych liter


def generate_password(request):
    length = request.GET.get("password_length")
    uppercase = request.GET.get("upper")
    numbers = request.GET.get("numbers")
    specials = request.GET.get("specials")

    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if specials:
        characters += string.punctuation

    password = ''
    for _ in range(int(length)):
        password += random.choice(characters)
    # password = ''.join(random.choice(characters) for _ in range(int(length)))
    return render(request, 'generate_password.html', {'password': password})
