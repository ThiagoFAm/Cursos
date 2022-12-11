#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.

def notas(nota_1, nota_2):
    
    media = int((nota_1 + nota_2)/2)

    return nota_1, nota_2, media

#Diferente dos outro exercícios, nesse usamos 'float' pelo fato de que a nota do boletim poderia estar em decimal.
n1 = float(input('Primeira Avaliação: '))
n2 = float(input('Segunda  Avaliação: '))

#Definindo variáveis para os valores retornados.

boletim = notas(n1, n2)

#Resultados.

print(f'1˚AV = {boletim[0]}\n2˚AV = {boletim[1]}\nMédia = {boletim[2]}')
