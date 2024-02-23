from Helpers.ColoramaHelpers import cy, r, g, b, y, m, lb, lc, lg, lm, ly, lr
from Helpers.ColoramaHelpers import p
from Helpers.ColoramaHelpers import c
from Examples.DragonCurve import DragonCurve 
from Examples.SierpinskiTriangle import SierpinskiTriangle
from Examples.KochCurve import KochCurve
from Examples.FractalBinaryTree import FractalBinaryTree
from Examples.FractalPlant import FractalPlant

def elegirModelo():

    """
        Le permite al usuario elegir un modelo. Regresa el numero del modelo
    """

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

def menu():

    p("Lindenmayer Systems", ly)
    p("")

    modelo = elegirModelo()

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
    menu()





        













