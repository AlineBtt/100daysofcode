#!/usr/bin/env python
# coding: utf-8

# ## Desafio Dia 02
# 
# Solicite o nome do usuário e imprima uma mensagem

# In[27]:


# Nome do usuário

nome_usuario = input("Digite seu nome: ")

# Mensagem
print("Olá,",nome_usuario,".", "I hope you have a good day." )


# #### Curso: Python: crie sua primeira aplicação
# 
#     "O Python é uma linguagem de programação de alto nível conhecida por sua simplicidade e versatilidade, e oferece um ambiente propício para o desenvolvimento de uma ampla gama de aplicações." - ALURA
#     
#     
#     Nome do Projeto - sabor-express
#     

# In[5]:


# Colocando o título da aplicação
print("Sabor Express\n")
    
# Cadastrando informaçÕes necessárias

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')


# In[6]:


# Recebendo dados com input e armazenar a opção na variavel: opcao_escolhida

opcao_escolhida = input("Escolha uma opção: ")
print('Você escolheu a opção', opcao_escolhida)


# "No Python, podemos definir uma variável qualquer e ela armazena o valor. Não precisamos informar explicitamente o tipo de variável que estamos definindo." - ALURA

# In[7]:


# Alterando o nome da aplicação - 
# Para colocar textos mais personalizados no terminal: https://fsymbols.com/pt/

print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


# "O Python oferece várias opções que podem ser usadas no print(), mas a f-string é bastante utilizada, pois podemos colocar a nossa variável diretamente dentro da string que estamos abrindo entre as aspas." - ALURA

# In[8]:


import this


# #### Exercises

# In[9]:


# Imprima a frase: Python na Escola de Programação da Alura.
print("Python na Escola de Programação da Alura.")

# Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome  = input("Qual seu nome?")
idade = input("Qual sua idade?") 

print("Meu nome é", nome, "e tenho", idade, "anos.")



# In[10]:


# Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
pi = 3.14159

print("O valor arredondado de pi é:", pi)


# Nesta aula, vimos os primeiros passos na linguagem, utilizando as funções print() e input() para passar e receber informações para o usuário.

# In[22]:


print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcao_escolhida)

if opcao_escolhida == 1:
   print('Cadastrar restaurante')
elif opcao_escolhida == 2:
   print('Listar restaurante')
elif opcao_escolhida == 3: 
   print('Ativar restaurante')
else: 
   print('Encerrando programa')


# #### Funções
# 
# 
# No lugar de escrevermos function, como acontece em algumas linguagens de programação, escrevemos def para definir a função.
# 
# import os

# def finalizar_app():
#     # os.system('cls')
#     s.system('clear') # no mac
#     print('Finalizando o app')

# In[ ]:


print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

def finalizar_app():
    s.system('clear')
    print('Finalizando o app')

if opcao_escolhida == 1:
   print('Cadastrar restaurante')
elif opcao_escolhida == 2:
   print('Listar restaurante')
elif opcao_escolhida == 3: 
   print('Ativar restaurante')
else: 
   finalizar_app()


# In[ ]:


# Próximo passo, colocando as opções dentro de funções

import os

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app()
os.system('clear')
print('Finalizando o app\n')

def escolher_opcao()

    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1:
    print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
    print('Listar restaurante')
    elif opcao_escolhida == 3: 
    print('Ativar restaurante')
    else: 
    finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': main()


# In[24]:


# Comando Match - oferece uma abordagem mais elegante para o uso do if else 

opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')


# In[ ]:




