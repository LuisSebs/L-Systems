from Grammar import Grammar

class FractalPlant(Grammar):

    def __init__(self, 
        title="Fractal Plant",
        number_iterations=6, 
        angle=25, 
        distance=5, 
        axiom="X", 
        rules={
            "X": "F+[[X]-X]-F[-FX]+X",
            "F": "FF"
        }
    ) -> None:
        super().__init__(title, number_iterations, angle, distance, axiom, rules)

    def draw_l_systems(self, some_turtle, instructions):

        some_turtle.hideturtle()

        some_turtle.left(45)

        stack_position = list()
        stack_angle = list()

        for task in instructions:
            if task == "F":
                some_turtle.forward(self.distance)
            elif task == "-":
                some_turtle.right(self.angle)
            elif task == "+":
                some_turtle.left(self.angle)
            elif task == "[":
                stack_position.append(some_turtle.position())
                stack_angle.append(some_turtle.heading())
            elif task == "]":
                some_turtle.up()
                some_turtle.setposition(stack_position.pop())
                some_turtle.down()
                some_turtle.setheading(stack_angle.pop())

