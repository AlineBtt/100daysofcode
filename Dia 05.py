#!/usr/bin/env python
# coding: utf-8

# ## Desafio Dia 05
# 
# Crie um programa que realize uma operação matemática simples (soma, subtração, multiplicação, divisão).
# 
# Este programa vai solicitar que o usuário insira dois números, mas o segundo número não pode ser igual a zero pois será utilizado em uma divisão.
# 

# In[ ]:


def obter_numero(mensagem, permitir_zero=False):
    while True:
        num = float(input(mensagem))
        if permitir_zero or num != 0:
            return num
        else:
            print('O número não pode ser igual a zero, tente novamente.')

num1 = obter_numero('Insira o primeiro número: ', permitir_zero=True)
num2 = obter_numero('Insira o segundo número: ')


# Agora, ao chamar obter_numero para o num1, você pode passar permitir_zero=True para permitir que num1 seja zero. Para num2, a validação padrão continua, garantindo que ele não seja zero.

# Após a coleta dos dois números, o programa abaixo faz a soma, subtração, multiplicação e divisão e apresenta os resultados.

# In[9]:


def operacao():
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    
    print("Soma:", soma)
    print("Subtração:", subtracao)
    print("Multiplicação:", multiplicacao)
    print("Divisão:", divisao)

operacao()


# ### Exercícios ALURA - docstring

# #### Crie uma docstring para a função exibir_nome_do_programa( )
# 
# '''Essa função exibe o nome do app na tela''''

# #### Crie uma docstring para a função exibir_opcoes( )
# 
# ''' Exibe as opções disponíveis no menu principal '''

# #### Crie uma docstring para a função finalizar_app( )
# 
# '''Exibe mensagem de finalização da aplicação'''

# #### Crie uma docstring para a função opcao_invalida( )
# 
# ''' Exibe mensagem de opção inválida e volta ao menu principal '''

# #### Crie uma docstring para a função exibir_subtitulo(texto)
# 
# '''  Exibe um subtítulo estilizado na tela 
#     
#   Inputs:
#     - texto: str - O texto do subtítulo '''

# #### Crie uma docstring para a função cadastrar_novo_restaurante( )
# 
# '''Essa função é responsável por cadastrar um novo restaurante
#     
#    Inputs:
#     - Nome do resturante
#     - Categoria
# 
#    Outputs:
#     -Adiciona um novo resturante na lista de restaurante
#     
#   '''

# #### Crie uma docstring para a função listar_restaurantes( )
# 
# '''Exibe uma lista com os restaurantes cadastrados 
# 
# Outputs:
#     - Exibe a lista de restaurantes na tela
# '''

# #### Crie uma docstring para a função alternar_estado_restaurante()
# 
# ''' Altera o estado ativo/desativado de um restaurante 
#     
# Outputs:
#     - Exibe mensagem indicando o sucesso da operação
# '''

# #### Crie uma docstring para a função escolher_opcao()
# 
# 
# ''' Solicita e executa a opção escolhida pelo usuário 
#     
#    Outputs:
#     - Executa a opção escolhida pelo usuário
#     '''

# #### Crie uma docstring para a função main()
# 
# ''' Função principal que inicia o programa '''
