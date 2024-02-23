import re
import sys
from Helpers.ColoramaHelpers import cy, r, g, b, y, m, lb, lc, lg, lm, ly, lr
from Helpers.ColoramaHelpers import p
from Helpers.ColoramaHelpers import c

from Examples.DragonCurve import DragonCurve 
from Examples.SierpinskiTriangle import SierpinskiTriangle
from Examples.KochCurve import KochCurve
from Examples.FractalBinaryTree import FractalBinaryTree
from Examples.FractalPlant import FractalPlant


def elegirModelo():
    while(True):

        strOpcion= c("[0]",lb) + " Fractal Binary Tree \n"+c("[1]",lb)+" Koch Curve\n"+c("[2]",lb)+" Sierpinski Triangle\n"+c("[3]",lb)+" Dragon Curve \n"+c("[4]",lb)+" Fractal Plant \n"
        p(strOpcion)
        opcion = input(c("Elige una opcion: ",lb))
        p("")
        if opcion == "0":
            return 0
        elif opcion == "1":
            return 1
        elif opcion == "2":
            return 2
        elif opcion == "3":
            return 3
        elif opcion == "4":
            return 4
        else:
            p("Elige una opcion valida", lr)

def infoModelo(modelo):

    if modelo == 0:
        print(FractalBinaryTree())
    elif modelo == 1:
        print(KochCurve())
    elif modelo == 2:
        print(SierpinskiTriangle())
    elif modelo == 3:
        print(DragonCurve())
    elif modelo == 4:
        print(FractalPlant())

def cambiarParametros():
    while True:

        p("¿Quieres cambiar los parametros del modelo?\n",ly)
        p(c("[0] ",lb)+"Si\n"+c("[1] ",lb)+"No\n")
        respuesta = input(c("Elige una opcion: ",lb))
        p("")
        
        if respuesta == "0":
            return 0
        elif respuesta == "1":
            return 1
        else:
            p("Elige una opcion valida", lr)

def agregarReglas():
    reglas = dict()
    while True:
        rule = input(c("regla: ",lb))
        left = re.search(r"[a-zA-Z0-9]{1}",rule).group()
        right = re.search(r"=[a-zA-Z0-9+-]+",rule).group()[1::]
        reglas[left]=right
        p(c("¿Quieres agregar otra regla?:\n",ly))
        p(c("[0] ",lb)+"Si\n"+c("[1] ",lb)+"No\n")
        respuesta = input(c("Elige una opcion: ",lb))
        if respuesta == "0":
            pass
        elif respuesta == "1":
            return reglas
        else:
            p("Elige una opcion valida", lr)
 
def nuevoModelo(modelo, iteraciones, distance, angulo, axioma, reglas):
    print(reglas)
    if modelo == 0:
        grammar = FractalBinaryTree("",iteraciones, angulo, distance, axioma, reglas)
        grammar.run(0,-200)
    elif modelo == 1:
        grammar = KochCurve("",iteraciones, angulo, distance, axioma, reglas)
        grammar.run(-200,0)
    elif modelo == 2:
        grammar = SierpinskiTriangle("",iteraciones, angulo, distance, axioma, reglas)
        grammar.run(-200,200)
    elif modelo == 3:
        grammar = DragonCurve("",iteraciones, angulo, distance, axioma, reglas)
        grammar.run(0,0)
    elif modelo == 4:
        grammar = FractalPlant("",iteraciones, angulo, distance, axioma, reglas)
        grammar.run(-320,-270)


def menu():

    p("Modo interactivo", ly)
    p("")

    modelo = elegirModelo()
    infoModelo(modelo)
    cambiar = cambiarParametros()

    if cambiar == 0:
        p("Ingresa los valores solicitados basados en el ejemplo: ", ly)
        p("")
        p("Ejemplo: ",y)
        p("")
        infoModelo(modelo=modelo)

        iteraciones = input(c("Iteraciones: ",lb))
        angulo = input(c("Angulo: ",lb))
        axioma = input(c("Axioma: ",lb))
        reglas = agregarReglas()

        nuevoModelo(modelo, int(iteraciones), int(angulo), 5, axioma, reglas)

    else:
        if modelo == 0:
            grammar = FractalBinaryTree()
            grammar.run(0,-200)
        elif modelo == 1:
            grammar = KochCurve()
            grammar.run(-200,0)
        elif modelo == 2:
            grammar = SierpinskiTriangle()
            grammar.run(-200,200)
        elif modelo == 3:
            grammar = DragonCurve()
            grammar.run(0,0)
        elif modelo == 4:
            grammar = FractalPlant()
            grammar.run(-320,-270)
        
        


if __name__ == "__main__":

    args = sys.argv

    if len(args) > 1 and len(args) < 3:
        if "0" in args:
            #grammar = FractalBinaryTree()
            #grammar.run(0,-200)
            print("Fractal Binary Tree")
        elif "1" in args:
            #grammar = KochCurve()
            #grammar.run(-200,0)
            print("Koch Curve")
        elif "2" in args:
            #grammar = SierpinskiTriangle()
            #grammar.run(-200,200)
            print("Sierpinski Triangle")
        elif "3" in args:
            #grammar = DragonCurve()
            #grammar.run(0,0)
            print("Dragon Curve")
        elif "4" in args:
            #grammar = FractalPlant()
            #grammar.run(-320,-270)
            print("Fractal Plant")
    else:
        menu()





        













