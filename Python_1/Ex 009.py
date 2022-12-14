#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

def tabuada(n): 
    #Como estamos usando um 'for', temos que criar uma lista.
    lista = []
    #Repetirá o programa até que ele seja rodado 11 vzs.
    for i in range(11):
        #Conta do produto.
        product = int(n * i)
        #Equação da tab.
        tab = (f'{i} x {n} = {product}')
        #método 'append' para adicionar o resultado de 'tab' na lista criada.
        lista.append(tab)
        
    return lista
#Definindo a lista como variável.
lista = tabuada(4)
print(lista)