from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mensagem

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