#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre as média.

def notas(nota_1, nota_2):
    
    media = int((nota_1 + nota_2)/2)

    return nota_1, nota_2, media

#Definindo variáveis para os valores retornados.

boletim = notas(n1, n2)

#Resultados.

print(f'Média = {boletim[2]}')
