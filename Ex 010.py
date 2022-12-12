#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar.
#Considere U$1.00 = R$3.27 // OBS = Valores representativos, não são reais.

def carteira(valor_dolar):
    RS = float(3.27) #Valor obtido para o Real 
    US = float(1.00) #Valor obtido para o Dólar. Por ser == a 1.0, não usamos o essa variável.
    valor_real = float(valor_dolar * RS) #Equação de conversão Dólar ----> Real
    print(f'Dólar = US ${valor_dolar} ----> Real = R${valor_real}') #Informando a conversão

    return valor_real #Retornando o valor do dolar convertido para real.

valor_dolar = float(input("Quantos dólares há em sua carteira? ")) #Entrada do valor do dólar
var = carteira(valor_dolar) #Armazenando o valor retornado da função em 'var'
print(f'Em sua carteira há R$ {round(var, 2)}') #'round()' é usado para limitar uma float
                                                #Assim determinamos que só irá mostrar 2 números depois do ponto.