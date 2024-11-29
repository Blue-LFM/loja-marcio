from django.shortcuts import render


def index(request):
    return render(request, 'aplicacao/index.html')


def categoria(request, categoria):
    context = {'nome': 'ERROR'}
    if categoria == 'pizzas':
        context = {
            'produtos': [{
                'nome': 'Pizza de frango',
                'descricao': 'Ingredientes: frango, massa branca, molho de tomate, orégano, queijo.',
                'imagem': '/static/aplicacao/imagens/pizza de frango.jpg',
                'preco': 6.00,
            },
                {
                'nome': 'Pizza de carne',
                'descricao': 'Ingredientes: carne, massa branca, molho de tomate, orégano, queijo.',
                'imagem': '/static/aplicacao/imagens/pizza de carne.jpg',
                'preco': 6.00,
            },
                {
                'nome': 'Pizza de calabresa',
                'descricao': 'Ingredientes: calabresa, massa branca, molho de tomate, orégano, queijo.',
                'imagem': '/static/aplicacao/imagens/pizza de calabresa.png',
                'preco': 6.00,
            },]
        }
    elif categoria == 'hamburgue-sanduiche':
        context = {
            'produtos': [{
                'nome': 'Hambúrger',
                'descricao': 'Ingredientes: pão, carne, alface, maionese.',
                'imagem': '/static/aplicacao/imagens/xis.jpeg',
                'preco': 6.00,
            },
                {
                'nome': 'Sanduíche de Frango',
                'descricao': 'Ingredientes: pão, frango, tomate, pepino, ovo cozido, maionese.',
                'imagem': '/static/aplicacao/imagens/sanduiche de frango.jpeg',
                'preco': 6.00,
            },
                {
                'nome': 'Sanduíche Integral',
                'descricao': 'Ingredientes: pão integral, frango, pepino, cenoura, maionese.',
                'imagem': '/static/aplicacao/imagens/sanduiche integral.jpg',
                'preco': 6.00,
            },
            {
                'nome': 'Sanduíche de Presunto',
                'descricao': 'Ingredientes: pão, presunto, tomate, queijo, alface, maionese.',
                'imagem': '/static/aplicacao/imagens/sanduiche de presunto.jpg',
                'preco': 6.00,
            },]
        }
    elif categoria == 'bolo-brigadeiro':
        context = {
            'produtos': [{
                'nome': 'Bolo de Chocolate',
                'descricao': 'Ingredientes: farinha, chocolate em pó, ovos, acúcar, leite, manteiga, fermento.',
                'imagem': '/static/aplicacao/imagens/bolo de chocolate.webp',
                'preco': 6.00,
            },
                {
                'nome': 'Brigadeiro',
                'descricao': 'Ingredientes: leite condensado, chocolate em pó, margarina sem sal, granulado.',
                'imagem': '/static/aplicacao/imagens/Brigadeiro.png',
                'preco': 4.00,
            },
                {
                'nome': 'Beijinho',
                'descricao': 'Ingredientes: leite condensado, coco ralado, margarina sem sal.',
                'imagem': '/static/aplicacao/imagens/beijinho.webp',
                'preco': 4.00,
            },]
        }
    elif categoria == 'suco':
        context = {
            'produtos': [{
                'nome': 'Sucos',
                'descricao': 'Sabores: morango, uva, maçã, abacaxi, entre outros.',
                'imagem': '/static/aplicacao/imagens/sucos.jpg',
                'preco': 3.50,
            },
                {
                'nome': 'Todinho',
                'descricao': 'Descrição: bebida de chocolate.',
                'imagem': '/static/aplicacao/imagens/todinho.webp',
                'preco': 2.50,
            },
                {
                'nome': 'Água com Gás',
                'descricao': 'Descrição: água com gás (bem auto-explicativo)',
                'imagem': '/static/aplicacao/imagens/agua com gas.webp',
                'preco': 3.50,
            },]
        }

    return render(request, 'aplicacao/categoria.html', context=context)


def index3(request):
    return render(request, 'aplicacao/index3.html')


def index4(request):
    return render(request, 'aplicacao/index4.html')


def index5(request):
    return render(request, 'aplicacao/index5.html')
