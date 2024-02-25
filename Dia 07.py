#!/usr/bin/env python
# coding: utf-8

# ## Desafio dia 07
# 
# Escreva um loop que imprima os números de 1 a 10.

# In[1]:


for i in range(1, 11):
    print(i)


# #### Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.

# In[ ]:


class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao


# In[ ]:


musica1 = Musica(nome='Quando bate aquela saudade', artista='Rubel', duracao=405)
musica2 = Musica(nome='Passarinhos', artista='Emicida', duracao=273)
musica3 = Musica(nome='One', artista='U2', duracao=273)


# #### Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

# In[2]:


class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


# ##### Instanciando um carro e atribuindo valores aos seus atributos

# In[3]:


meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)


# #### Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

# In[ ]:


class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao


# #### Instanciando um restaurante e atribuindo valores aos seus atributos

# In[ ]:


restaurante_exemplo = Restaurante(nome='Comida Boa', categoria='Gourmet', ativo=True, capacidade=50, nota_avaliacao=4.5)


# In[ ]:




