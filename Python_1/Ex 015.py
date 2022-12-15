#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

def aluguel(km, dias):
    km_rodado = float(km * 0.15)
    dias_usados = float(dias * 60)

    return km_rodado, dias_usados

km = float(input('Quantos kilometros rodados: '))
dias = float(input('Dias que o carro ficou sobre posse do indivíduo: '))

km_rodado, dias_usados = aluguel(km, dias)

print(f'O carro percorreu {km}Km durante {dias} dia(s)\nPortanto o valor a ser cobrado é de R${km_rodado + dias_usados}')
