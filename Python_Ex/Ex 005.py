#Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e seu sucessor.

n = int(input('Digite o número desejado: '))

def num(meio):
    antecessor = int(meio - 1)
    sucessor   = int(meio + 1)

    #print(f'{antecessor} -- {meio} -- {sucessor}')

    #Retornando as variáveis.
    return antecessor, meio, sucessor

#Definindo o número a ser usado no código.



num(n)

#Definindo variáveis para os valores retornados.

#1˚ método:

#vars = num(Insira aqui o número desejado) Dessa forma agrupamos as três variáveis que são geradas na função

#print(vars[0]\nvars[1]\nvars[2])

#2˚ método:

ant, meio, suc = num(n) #Dessa forma não agrupamos em uma só variável, mas definimos uma variável para cada.

print(f'Antecessor = {ant}\nMédio      = {meio}\nSucessor   = {suc}')