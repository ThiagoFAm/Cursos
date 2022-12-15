#Um professor quer sortear um dos seus alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random #Lib que diz respeito a aleatóridade de números.

alunos = ['Carl','Jeff','Erich','Mason'] #lista com os nomes.

def sorteio(): #Função
    
    num_sort = random.randrange(0,4) #'randrange' está sorteia um número de 0 a 3.
    
    aluno_sort = alunos[num_sort] #Usa o número sorteado como localizador na lista.

    print(f'O aluno sorteado foi {aluno_sort}') #Imprimindo o resultado

    return aluno_sort #Retornando o aluno sorteado

aluno = sorteio() #Armazenando a variável retornada em 'aluno'