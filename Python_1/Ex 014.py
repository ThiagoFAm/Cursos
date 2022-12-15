#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

def conversor_temp(C):
    F = (9/5 * C) + 32

    return C, F

C = float(input('Digite a tempratura em Celsius: '))
cel, far = conversor_temp(C)

print(f'Celsius = {C}\nFareheint = {far}')