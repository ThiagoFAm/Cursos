import math


def trigonometria(a):

    seno = math.sin(math.radians(a))
    cosseno = math.cos(math.radians(a))
    tangente = math.tan(math.radians(a))
    print("O seno do ângulo é",seno,"o cosseno é",cosseno,"e a tangente é",tangente)


a = int(input("Digite o ângulo: "))