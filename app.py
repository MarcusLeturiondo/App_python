# -*- coding UTF-8 -*-
def listar(nomes):
    print 'Listando nomes: '
    for nome in nomes:
        print nome

def cadastrar(nomes):
    print 'Digite seu nome: '
    nome = raw_input()
    nomes.append(nome)

def procurar(nomes):
    print 'Qual nome voce procura?'
    nome = raw_input()

    if(nome in nomes):
        print 'O %s  ja esta cadastrado' % (nome)
    else:
        print 'O %s ainda nao foi cadastrado' % (nome)

def remover(nomes):
    print 'Qual nome voce quer excluir?'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome voce quer alterar?'
    nome_a_remover = raw_input()

    if(nome_a_remover in nomes):
        posicao = nomes.index(nome_a_remover)
        print 'Digite o novo Nome: '
        nome_novo = raw_input()
        nomes[posicao] = nome_novo

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite: 1 - Cadastrar, 2 - Listar, 3 - Procurar, 4 - Alterar, 5 - Excluir e 0 - Terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            procurar(nomes)
        if(escolha == '4'):
            alterar(nomes)
        if(escolha == '5'):
            remover(nomes)
menu()
