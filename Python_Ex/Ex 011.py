#Faça um programa que leia a largura e a altura de uma parede em metros. 
#Calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta pinta uma área de 2m2(dois metros quadrados).

def parede(largura, altura):
    tinta = float(2) #Cada 1L pinta 2m2.
    area_parede = float(largura * altura) #A parede é um quadrado, ou seja, usaremos a área do quadrado(lado * lado).
    qtd_necessária = float(area_parede/tinta) #Equação para descobrir quantos Litros de tinta serão necessários.

    return area_parede, qtd_necessária #Retornando as váriaveis.

area_parede, litros_necessario = parede(largura, altura) #Armazenando os resultados retornados em area, litros. Respectivamente.

print(litros_necessario, area_parede)
