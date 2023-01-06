#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos kilometros rodados: ')) #entrada km.
dias = float(input('Dias que o carro ficou sobre posse do indivíduo: ')) #Entrada dias.

def aluguel(km, dias): #Função
    
    km_rodado = float(km * 0.15) #Kilometros rodados multiplicado por 15 centavos.
    dias_usados = float(dias * 60) #Dia(s) multiplicado por 60.

    print(f'O carro percorreu {km}Km durante {dias} dia(s)\nPortanto o valor a ser cobrado é de R${km_rodado + dias_usados}')

    return km_rodado, dias_usados #Retorno das variáveis.

km_rodado, dias_usados = aluguel(km, dias) #Armazenando os retornos em variáveis respectivas.