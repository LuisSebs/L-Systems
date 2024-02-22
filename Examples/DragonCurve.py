from Grammar import Grammar

class DragonCurve(Grammar):
    
    def __init__(self, 
        number_iterations=10, 
        angle=90, 
        distance=5, 
        axiom="F", 
        rules = {
            "F": "F+G",
            "G": "F-G"
        } ) -> None:
        super().__init__(number_iterations, angle, distance, axiom, rules)

    def draw_l_systems(self, some_turtle, instructions):
        for task in instructions:
            if task == 'F':
                some_turtle.forward(self.distance)
            elif task == 'G':
                some_turtle.backward(self.distance)
            elif task == '+':
                some_turtle.left(self.angle)
            elif task == '-':
                some_turtle.right(self.angle)



    