import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma(numero1, numero2):
    sum = numero1 + numero2
    return sum


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares():
    return 0


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro(radio, altura):
    areaLateral = 2 * radio * math.pi * radio * altura
    areaCirculo = 2 * radio * math.pi * radio * radio
    result = areaLateral + areaCirculo
    return result


def areaLateral(radio, altura):
    result = 2 * radio * math.pi * radio * altura
    return result


def areaCirculo(radio, altura):
    result = 2 * radio * math.pi * radio ** 2
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
    def areaTotalCilindro(self):
        return 0


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    self.Restaurante = []

    def ordenar(self, nombre, lugar, costo, conDescuento, descuento):
        self.restaurante = (self, nombre, lugar, costo, conDescuento, descuento)
        self.Restaurante.append(self.restaurante)
        return self.restaurante

    def costoTotal(self):
        return 0

    def costoTotalConDescuento(self):
        return 0


class Pizza:
    nombre = input("Ingrese su nombre: ")
    lugar = input("Ingrese un lugar: ")
    costo = float(input("Ingrese el costo"))
    conDescuento = input("Tiene descuento? ")
    if conDescuento == "no":
        print(False)
    else:
        print(True)
    if conDescuento == "no":
        print("no hay descuento")
    else:
        descuento = input("Cual es el descuento?: ")
        print("hay descuento")


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
