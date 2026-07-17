from manim import *

class CreateCircleAndSquare(Scene):
    def construct(self):
        # 1. Create a pink circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        
        # 2. Animate the circle appearing on screen
        self.play(Create(circle))
        self.wait(1)

        # 3. Create a blue square
        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        # 4. Transform the circle into the square
        self.play(Transform(circle, square))
        self.wait(1)

        # 5. Add and display text
        text = Text("Hello, Manim!")
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(1)
