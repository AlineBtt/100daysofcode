#!/usr/bin/env python
# coding: utf-8

# ## Desafio Dia 04 
# Faça um programa que solicite dois números ao usuário, some-os e imprima o resultado

# In[1]:


## Solicitar os números

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

## Somando os números

soma = num1 + num2 

## Resultado

print("A soma dos números é:", soma)


# ## Exercicios

# ### 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
# 
# 

# In[22]:


pessoa = {  'Nome': 'Aline'
          , 'Idade':33
          , 'Cidade':'Londrina'}

print(pessoa['Nome'], '|', pessoa['Idade'], '|', pessoa['Cidade'])


# ### 2 - Utilizando o dicionário criado no item 1:
# 
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário

# In[13]:


## Alterando a idade
pessoa['Idade'] = 34
pessoa


# In[15]:


## deletando a cidade

del pessoa['Cidade']
pessoa


# In[17]:


pessoa['Profissão'] = 'Estatística'
pessoa


# ### 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

# In[19]:


num_e_quadrados = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

print(num_e_quadrados)


# In[20]:


numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


# ### 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# In[23]:


if 'Nome' in pessoa:
    print("A chave 'Nome' existe no dicionário.")
else:
    print("A chave 'Nome' não existe no dicionário.")


# ### 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

# In[34]:


frase = "O rato roeu a cama e o rato roeu a roupa."


# In[35]:


def contar_frequencia_palavras(frase):
    
    # Remover pontuações e converter para minúsculas
    frase = frase.lower().replace('.', '').replace(',', '')
    # Dividir a frase em palavras
    palavras = frase.split()
    # Inicializar o dicionário para armazenar a contagem de palavras
    frequencia_palavras = {}
    # Contar a frequência de cada palavra
    for palavra in palavras:
        if palavra in frequencia_palavras:
            frequencia_palavras[palavra] += 1
        else:
            frequencia_palavras[palavra] = 1

    return frequencia_palavras


# In[36]:


resultado = contar_frequencia_palavras(frase)


# In[37]:


# Exibindo o resultado
for palavra, frequencia in resultado.items():
    print(f'A palavra "{palavra}" aparece {frequencia} vezes.')


# In[ ]:




