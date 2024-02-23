from Grammar import Grammar

class KochCurve(Grammar):

    def __init__(self, 
        title="Koch Curve",
        number_iterations=4, 
        angle=90, 
        distance=5, 
        axiom="F++F++F", 
        rules={
            "F": "F+F-F-F+F"
        }
    ) -> None:
        super().__init__(title, number_iterations, angle, distance, axiom, rules)

    def draw_l_systems(self, some_turtle, instructions):
        for task in instructions:
            if task == "F":
                some_turtle.forward(self.distance)
            elif task == "+":
                some_turtle.left(self.angle)
            elif task == "-":
                some_turtle.right(self.angle)