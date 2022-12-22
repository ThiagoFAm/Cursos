#Crie um programa que leia um número qualquer pelo teclado e mostre sua porção inteira.

import math #modulo matemático.

def mat(num): #função
    
    num_trunc = math.trunc(num) #trunc, método que extrai a parte inteira de um numero decimal.

    print(f'A parte inteira do número {num} é {num_trunc}') #Imprimindo o resultado.

    return num, num_trunc #retornando os valores.

num = float(input('Digite um número: ')) #Entrada do número a ser 'transformado'.

num_float, num_int = mat(num) #Armazenando os retornos em suas respectivas variáveis.