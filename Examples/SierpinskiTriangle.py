from Grammar import Grammar

class SierpinskiTriangle(Grammar):

    def __init__(self, 
        title="Sierpinski Triangle",
        number_iterations=6, 
        angle=120, 
        distance=5, 
        axiom="F-G-G", 
        rules={
            "F": "F-G+F+G-F",
            "G": "GG"
        }
    ) -> None:
        super().__init__(title, number_iterations, angle, distance, axiom, rules)

    def draw_l_systems(self, some_turtle, instructions):
        for task in instructions:
            if task == "F":
                some_turtle.forward(self.distance)
            elif task == "G":
                some_turtle.forward(self.distance)
            elif task == "+":
                some_turtle.left(self.angle)
            elif task == "-":
                some_turtle.right(self.angle)