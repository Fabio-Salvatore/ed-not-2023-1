"""
 Função para calcular o índice da Massa Corpórea
 de uma pessoa , dados o seu peso e sua altura
"""
def imc (peso, altura):
    # Peso dividido pela altura elevada ao quadrado
    return peso / altura ** 2

resultado = imc(99,1.75)

print("O imc calculado é ",resultado)

##################################################################

from math import pi

def calcular_area(base, altura , tipo):
    if tipo == "R":   #Retangulo
        return base * altura
    elif tipo == "T": #Triangulo
        return base * altura /2
    elif tipo == "E": #Elipse ou circulo
     return (base / 2) * (altura /2) * pi
    else:
        return None




 