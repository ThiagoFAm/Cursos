#Crie um programa que leia um número qualquer pelo teclado e mostre sua porção inteira.

import math

def mat(num):
    
    num_trunc = math.trunc(num)

    print(f'A parte inteira do número {num} é {num_trunc}')

    return num, num_trunc

num = float(input('Digite um número: '))

num_float, num_int = mat(num)