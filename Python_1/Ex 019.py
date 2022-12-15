#Um professor quer sortear um dos seus alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

alunos = ['Carl','Jeff','Erich','Mason']

def sorteio():
    
    num_sort = random.randrange(0,4)
    
    aluno_sort = alunos[num_sort]

    print(f'O aluno sorteado foi {aluno_sort}')

    return aluno_sort

aluno = sorteio()