#!/usr/bin/env python
# coding: utf-8

# ## Desafio Dia 06
# 
# Crie um programa que determine se um número é par ou ímpar.

# In[1]:


# Função para verificar se um número é par ou ímpar
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Solicita ao usuário que insira um número
numero_inserido = int(input("Digite um número: "))

resultado = verificar_paridade(numero_inserido)
print(f"O número {numero_inserido} é {resultado}.")


# Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados. - ALURA

# Crie uma classe chamada Musica com os seguintes atributos: nome, artista, duração e crie 3 objetos definindo cada atributo.

# In[13]:


class Musica:
    def __init__(self, nome='', artista='', duracao=0, categoria=''):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.categoria = categoria


# In[14]:


musica1 = Musica(nome='Quando bate aquela saudade', artista='Rubel', duracao=405)
musica2 = Musica(nome='Passarinhos', artista='Emicida', duracao=273)
musica3 = Musica(nome='One', artista='U2', duracao=273)


# In[17]:


### Atribuindo a categoria rock para a música one

musica3.categoria = 'Rock'


# In[19]:


### Acessando um atributo na musica 1

Artista = musica1.artista
Artista


# In[22]:


### Verifica se a música 3 é rock

if musica3.categoria == 'Rock':
    print('A categoria da música é rock')
else:
    print('A categoria da música não é rock')


# ### Instância de uma classe

# #### Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

# restaurante_praca.categoria = 'Italiana'

# #### Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

# nome_do_restaurante = restaurante_praca.nome

# #### Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

# In[ ]:


if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')


# #### Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.

# categoria = Restaurante.categoria

# #### Altere o valor do atributo nome para 'Bistrô'.

# restaurante_praca.nome = 'Bistrô'

# #### Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

# restaurante_pizza = Restaurante()
# 
# restaurante_pizza.nome = 'Pizza Place'
# restaurante_pizza.categoria = 'Fast Food'

# #### Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

# In[ ]:


if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')


# #### Mude o estado da instância restaurante_pizza para ativo.

# restaurante_pizza.ativo = True

# #### Imprima no console o nome e a categoria da instância restaurante_praca.

# In[ ]:


print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')

