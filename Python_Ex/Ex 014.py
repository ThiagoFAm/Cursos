#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

def conversor_temp(C): #Função.
    F = (9/5 * C) + 32 #Equação de conversão.

    return C, F #Retorno.

C = float(input('Digite a tempratura em Celsius: ')) #Entrada com float.
cel, far = conversor_temp(C) #Armazendo os retornos respectivamente.

print(f'Celsius = {C}\nFareheint = {far}') #Imprimindo o Resultado.