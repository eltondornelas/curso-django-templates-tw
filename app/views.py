from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    nome_da_empresa = 'treinaWeb'
    descricao = 'Há mais de 12 anos formando desenvolvedores de ponta! ' \
                'São mais de 4.000 horas de conteúdo, com formações ' \
                'completas e com foco no mercado de trabalho. '

    contato_empresa = {
        'endereco': ' Av. Paulista, 1765, Conj 71 e 72 - Bela Vista -'
                    ' São Paulo - SP - 01311-200 ',
        'telefone': '12345678',
        'email': 'contato@treinaweb.com.br'
    }

    cursos_home = {
        '1': {'titulo': 'Django Fundamentos',
              'descricao': 'Aprenda toda a base de Django!'},
        '2': {'titulo': 'Flask Fundamentos',
              'descricao': 'Aprenda toda a base de Flask!'},
        '3': {'titulo': 'Python OO', 'descricao': 'Aprenda OO com Python !'},
    }

    return render(request, 'empresa/index.html',
                  {'nome_empresa': nome_da_empresa,
                   'descricao_empresa': descricao,
                   'contato_empresa': contato_empresa,
                   'cursos_home': cursos_home})


def about(request):
    return render(request, 'empresa/about.html')


def contact(request, id):
    return render(request, 'empresa/contact.html')
