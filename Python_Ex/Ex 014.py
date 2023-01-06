#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

C = float(input('Digite a tempratura em Celsius: ')) #Entrada com float.

def conversor_temp(C): #Função.
    F = (9/5 * C) + 32 #Equação de conversão.

    print(f'Celsius = {C}\nFareheint = {far}') #Imprimindo o Resultado.

    return C, F #Retorno.

cel, far = conversor_temp(C) #Armazendo os retornos respectivamente.