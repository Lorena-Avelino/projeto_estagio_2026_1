from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mensagem

from django.contrib.auth.decorators import login_required

def landpage(request):
    if request.method == 'POST':
        nome = (request.POST.get("nome") or "").strip()
        email = (request.POST.get('email') or "").strip()
        texto = (request.POST.get('mensagem') or "").strip()

        if nome and email and texto:
            mensagem = Mensagem(nome=nome, email=email, mensagem=texto)
            mensagem.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('landpage')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'landpage.html')

@login_required(login_url="login")
def painel_mensagens(request):
    mensagens = Mensagem.objects.all().order_by("-data_envio")
    return render(request, "painel.html", {"mensagens": mensagens})