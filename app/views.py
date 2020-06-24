from django.shortcuts import render


def index(request):
    nome_da_empresa = 'TreinaWeb'
    descricao = 'Há mais de 12 anos formando desenvolvedores de ponta! ' \
                'São mais de 4.000 horas de conteúdo, com formações ' \
                'completas e com foco no mercado de trabalho. '

    contato_empresa = {
        'endereco': ' Av. Paulista, 1765, Conj 71 e 72 - Bela Vista -'
                    ' São Paulo - SP - 01311-200 ',
        'telefone': '12345678',
        'email': 'contato@treinaweb.com.br'
    }

    return render(request, 'empresa/index.html',
                  {'nome_empresa': nome_da_empresa,
                   'descricao_empresa': descricao,
                   'contato_empresa': contato_empresa})
