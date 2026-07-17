from manim import *

class xd123(Scene):
    def construct(self):
        rect1 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1).shift(LEFT*5)
        rect2 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1).move_to([5, 0, 0])

        r1 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
        r2 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
        r3 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
        r4 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
        r5 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)

        group = VGroup(r1, r2, r3, r4, r5)
        group.arrange()
        group.set_color_by_gradient(RED, ORANGE, YELLOW_C, PURE_GREEN)

        self.play(Write(rect1))
        self.play(Write(rect2))

        g2= VGroup(rect1, rect2)

        self.play(rect2.animate.next_to(rect1, RIGHT))
        self.play(ReplacementTransform(g2, group))

        s1 = SurroundingRectangle(group, color = WHITE)
        s2 = SurroundingRectangle(s1, color = WHITE)

        self.play(Write(s1), Write(s2, run_time = 1.5))

        t = Text("1 2 3 4 5").next_to(s2, UP, buff = 0.3).scale(1.5)
        self.play(Write(t))

        self.play(Indicate(t[0], color = RED), Indicate(r1, color = RED, scale_factor = 0.3))
        self.play(Indicate(t[1], color = RED), Indicate(r2, color = RED, scale_factor = 0.3))
        self.play(Indicate(t[2], color = RED), Indicate(r3, color = RED, scale_factor = 0.3))
        self.play(Indicate(t[3], color = RED), Indicate(r4, color = RED, scale_factor = 0.3))
        self.play(Indicate(t[4], color = RED), Indicate(r5, color = RED, scale_factor = 0.3))

        d = Dot(color = RED)

        g3 = VGroup(group, t, s1, s2)

        self.play(ReplacementTransform(g3, d))
        self.play(d.animate.scale(150))
        self.play(FadeOut(d))
        self.wait(3)