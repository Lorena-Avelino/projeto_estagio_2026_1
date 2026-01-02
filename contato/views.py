from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mensagem
from django.db.models import Q

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
    q = (request.GET.get("q") or "").strip()
    mensagens = Mensagem.objects.all()
    if q:   
        mensagens = mensagens.filter(
            Q(nome__icontains=q) |
            Q(email__icontains=q) |
            Q(mensagem__icontains=q)
        )
    mensagens = mensagens.order_by('-data_envio')
    return render(request, "painel.html", {"mensagens": mensagens, "q": q})