#!/usr/bin/env python
# coding: utf-8

# ## Desafio Dia 03 
# 
# Crie uma lista com alguns itens e imprima cada um deles

# In[2]:


## Criando uma lista

Lasanha  = ["Massa de Lasanha sem glúten", "Carne Moída", "Molho de Tomate", "Creme de Leite"]
Temperos = ["Pimenta","Sal","Noz-moscada","Páprica"]

print("Lista de Ingredientes:", Lasanha + Temperos)


# ## Exercícios

# #### 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
# 

# In[9]:


def par_impar():
    numero = int(input("Escreva um número inteiro: "))
    if numero % 2 == 0:
        print(f"{numero} é um número par")
    else: 
        print(f"{numero} é um número ímpar")
        
par_impar()


# #### 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# 
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
# 

# In[14]:


def idade_class ():
    idade = int(input("Qual sua idade? "))
    if idade <= 12:
        print("Você é uma criança")
    elif idade < 18:
        print("Você é adolescente")
    elif:
        print("Você é adulto")
    else:
        print("Valor Inválido")
    
        
idade_class()


# #### 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
# 
# 

# In[20]:


def user_senha():
    user  = input("Qual o nome do usuário? ")
    senha = input("Insira sua senha: ")
    if user == "Aline" and senha == "Senha123":
        print("Acesso garantido! Seja bem-vinda,", user)
    else:
        print("Acesso negado")    

user_senha()
    


# #### 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# 
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# In[24]:


def local_ponto():
    x = float(input("Insira o valor do ponto no eixo x: "))
    y = float(input("Insira o valor do ponto no eixo y: "))
    if x > 0 and y > 0:
        print("Este ponto está no primeiro quadrante")
    elif x < 0 and y > 0:
        print("Este ponto está no segundo quadrante")
    elif x < 0 and y < 0:
        print("Este ponto está no terceiro quadrante")
    elif x > 0 and y < 0:
        print("Este ponto está no quarto quadrante")
    else:
        print("O ponto está localizado na origem")
        
local_ponto()


# ## Exercicios Módulo 3

# #### 1 - Crie uma lista para cada informação a seguir:
# 
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
# 

# In[27]:


# A função range() no Python é usada para gerar uma sequência de números. 

numeros_1a10 = list(range(1,11))
numeros_1a10


# In[28]:


nomes = ['Joana', 'Mariana', 'Melissa', 'Jurema' ]
nomes


# In[29]:


ano_nasc_atual = [1990, 2024]
ano_nasc_atual


# #### 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# In[32]:


lista = list(range(1,11))
for elemento in lista:
    print(elemento)


# #### 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# In[42]:


somar_impares = 0 
    
for numero in range(1,11,2):
    somar_impares += numero

print('A soma dos números ímpares é:', somar_impares)


# #### 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# In[47]:


for numero in range(10,0,-1):
    print(numero)


# #### 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# In[52]:


numero = int(input('Digite um número: '))

print(f'Tabuada do {numero}:')
for i in range(1,11):
    resultado = numero * i 
    print(f'{numero} * {i} = {resultado}')
             


# #### 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# Exception é uma classe base para todas as exceções em Python. Capturar Exception permite lidar com qualquer tipo de exceção que possa ocorrer no bloco try. O as e é opcional, mas é frequentemente usado para acessar informações detalhadas sobre a exceção, como mensagens de erro.

# In[65]:


lista = list(range(1,30))
somar_numeros = 0

try:
    for i in lista:
        somar_numeros += numero
except TypeError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
else:
    print(f"A soma dos elementos é: {somar_numeros}")


# #### 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

# ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão por zero. Este bloco except é destinado a lidar especificamente com esse tipo de erro.

# In[76]:


def calcular_media(lista):
    
    try:
        if not lista:
            raise ValueError("A lista está vazia.")
        
        media = sum(lista)/len(lista)
        print('A média dos números na lista é', media)
    except ZeroDivisionError:
        print('A lista está vazia.')
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

        
lista = list(range(1,20,3))
print('Os números selecionados são:', lista)

media = calcular_media(lista)


# Casos com lista vazia, não é possível calcular a média
lista2 = []
calcular_media(lista2)
        


# In[ ]:




