#!/usr/bin/env python
# coding: utf-8

# # Desafio Dia 09 
# 
# Crie um programa que inverta uma string

# In[1]:


def inverter_string(s):
    return s[::-1]


# In[6]:


entrada = input("Digite uma string: ")


# In[7]:


resultado = inverter_string(entrada)
print("String invertida:", resultado)


# ---------------------------------

# ## Exercicios

# Faça um programa que vende uma garrafa de água:
# 
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# 
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# 

# In[21]:


def vender_agua(tipo_agua):
    if tipo_agua == "natural":
        preco = 1.50
    elif tipo_agua == "com gás":
        preco = 2.50
    else:
        print("Opção inválida. Escolha entre 'natural' ou 'com gás'.")
        return

    print(f"Você escolheu água mineral {tipo_agua}. O total a ser pago é R${preco:.2f}.")


# In[22]:


tipo_escolhido = input("Escolha o tipo de água ('natural' ou 'com gás'): ").lower()


# In[23]:


vender_agua(tipo_escolhido)


# ##### Altere o programa anterior para considerar a quantidade de água
# 

# In[28]:


def vender_agua(tipo_agua, quantidade):
    if tipo_agua == "natural":
        preco_unitario = 1.50
    elif tipo_agua == "com gás":
        preco_unitario = 2.50
    else:
        print("Opção inválida. Escolha entre 'natural' ou 'com gás'.")
        return
    
    total_pagar = quantidade * preco_unitario
    print(f"Você escolheu água mineral {tipo_agua}. O total a ser pago por {quantidade} garrafa(s) é R${total_pagar:.2f}.")


# In[29]:


tipo_escolhido = input("Escolha o tipo de água ('natural' ou 'com gás'): ").lower()
quantidade_escolhida = int(input("Quantas garrafas você deseja comprar? "))


# In[30]:


vender_agua(tipo_escolhido, quantidade_escolhida)


# #### Faça o programa de uma sorveteria, onde o usuário pode escolher:
# 
# Tipo de sorvete: 
# casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# 
# Sabor do sorvete: morango, creme, chocolate
# 
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# 
# Apresente o valor a ser pago
# 

# In[47]:


def calcular_valor_sorvete(tipo_sorvete, sabor, cobertura):
    # Definindo os preços
    precos_tipo = {"casquinha": 1.00, "cascão": 2.50, "cestinha": 4.00}
    precos_cobertura = {"caramelo": 1.50, "morango": 1.50, "chocolate": 1.50, "sem cobertura": 0.00}
    
    if tipo_sorvete not in precos_tipo or cobertura not in precos_cobertura:
        print("Opção inválida. Por favor, escolha opções válidas.")
        return
# Calculando o valor total
        valor_tipo = precos_tipo[tipo_sorvete]
        valor_cobertura = precos_cobertura[cobertura]
        valor_total = valor_tipo + valor_cobertura
        
        print(f"Você escolheu sorvete {tipo_sorvete} sabor {sabor} com cobertura de {cobertura}. O total a ser pago é R${valor_total:.2f}.") 


# In[ ]:


# Solicita ao usuário que faça suas escolhas
tipo_sorvete = input("Escolha o tipo de sorvete (casquinha, cascão, cestinha): ").lower()
sabor_sorvete = input("Escolha o sabor do sorvete (morango, creme, chocolate): ").lower()
cobertura_sorvete = input("Escolha a cobertura do sorvete (caramelo, morango, chocolate, sem cobertura): ").lower()


# In[ ]:


# Chama a função para calcular o valor com base nas escolhas do usuário
calcular_valor_sorvete(tipo_sorvete, sabor_sorvete, cobertura_sorvete)


# In[ ]:




