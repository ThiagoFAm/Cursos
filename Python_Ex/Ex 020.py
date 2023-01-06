#O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalho de alunos.
#Faça um programa que leia o número dos qautro alunos e mostre a oredem sorteada.

import random

alunos = ['Carl','Jeff','Erich','Mason'] #Alunos.

def sort_order(): #Função.

    ord = random.sample(alunos, k=len(alunos))

    print(ord) #Método 'sample' da lib random é usado para embaralhar uma ordem.

    print(ord)

    return ord #Retorno da var.

order_sort = sort_order() #Armazenando o resultado em uma var.

