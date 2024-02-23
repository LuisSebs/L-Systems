from Grammar import Grammar

class FractalBinaryTree(Grammar):

    def __init__(self,
        title="Fractal Binary Tree",
        number_iterations=6, 
        angle=45, 
        distance=5, 
        axiom="0", 
        rules={
            "1": "11",
            "0": "1[0]0"
        }
        ) -> None:
        super().__init__(title, number_iterations, angle, distance, axiom, rules)
    
    def draw_l_systems(self, some_turtle, instructions):

        some_turtle.hideturtle()
        some_turtle.left(90)

        stack_position = list()
        stack_angle = list()
        
        for task in instructions:
            if task == "0":
                some_turtle.forward(self.distance)
            elif task == "1":
                some_turtle.forward(self.distance)
            elif task == "[":
                stack_position.append(some_turtle.position())
                stack_angle.append(some_turtle.heading())
                some_turtle.left(self.angle)
            elif task == "]":
                some_turtle.up()
                some_turtle.setposition(stack_position.pop())
                some_turtle.down()
                some_turtle.setheading(stack_angle.pop())
                some_turtle.right(self.angle)
