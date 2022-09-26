from manim import *

class Testing(Scene):
    def construct(self):
        name=Tex("Carlos Raúl").to_edge(UR, buff=0.5)
        
        sq=Square(
            side_length=2, stroke_color=BLUE, fill_color=WHITE, fill_opacity=0.5 
        ).shift(LEFT*3)
        
        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time=3)
        self.wait()
