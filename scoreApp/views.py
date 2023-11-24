from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email_login")
        password = request.POST.get("senha_login")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("inicio")  # Redirecionamento para a página 'inicio'

        else:
            messages.error(request, "E-mail ou senha inválidos.")

    return render(request, "Login.html")


def cadastrar_usuario(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if not User.objects.filter(username=email).exists():
            novo_usuario = User.objects.create_user(
                username=email, email=email, password=senha
            )
            novo_usuario.save()
            messages.success(request, "Usuário cadastrado com sucesso!")

        else:
            messages.error(request, "Esse usuário já existe.")

    return render(request, "Login.html")


# Garante que apenas usuários autenticados acessem essa view
def inicio(request):
    usuario = request.user
    return render(request, "inicio.html", {"usuario": usuario})
