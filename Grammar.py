import turtle
import colorama
from abc import ABC, abstractclassmethod
from Helpers.ColoramaHelpers import cy, r, g, b, y, m, lb, lc, lg, lm, ly, lr
from Helpers.ColoramaHelpers import p
from Helpers.ColoramaHelpers import c

class Grammar(ABC):

    """
        Grammar for Lindenmayer System
    """

    def __init__(self, title, number_iterations, angle, distance, axiom, rules) -> None:
        self.title = title
        self.number_iterations = number_iterations
        self.angle = angle
        self.distance = distance
        self.axiom = axiom
        self.rules = rules

    def __str__(self) -> str:
        result = c(self.title, cy)+":\n\n"
        result += "Iteraciones: "+c(str(self.number_iterations), lg)+"\n"
        result += "Angulo: "+c(str(self.angle), lg)+"\n"
        result += "Axiom: "+c(self.axiom, lg)+"\n"
        result += "Rules:\n\n"
        for key in self.rules.keys():
            result += " "+key+c("=",y)+c(self.rules[key])+"\n"
        return result 

    def appy_rules(self, letter):
        """
            Apply rules to an individual letter, an return the result.
        """
        if letter in self.rules:
            return self.rules[letter]
        else:
            return letter

    def process_string(self, original_string):
        """
            Apply rules to a string, one letter at a time, an return the result.
        """
        transformed_string = ""
        for letter in original_string:
            transformed_string = transformed_string + self.appy_rules(letter)

        return transformed_string

    def create_l_system(self):
        """
            Begin with an axiom, and apply rules to the original axiom string
            number_of_iterations times, then return the result.
        """
        start_string = self.axiom
        for _ in range(self.number_iterations):
            end_string = self.process_string(start_string)
            start_string = end_string
        
        return end_string
    
    @abstractclassmethod
    def draw_l_systems(self, some_turtle, instructions):
        """
            Draw with some_turtle, interpreting each letter in the instructions passed in.
        """
        pass

    def run(self, x=0, y=0):
        """
            Run graphic turtle
        """
        window = turtle.Screen()
        t = turtle.Turtle()
        t.speed(0)
        t.up()
        t.setposition(x,y)
        t.down()
        instruction_string = self.create_l_system()
        self.draw_l_systems(t, instruction_string)
        turtle.Screen().exitonclick()