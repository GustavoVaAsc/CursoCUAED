from manim import *

class EjeX(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"
        
        # Colores del archivo
        #cyan = "#FF66C4"
        #purple = "#007BFF"
        cyan = "#00FFFF"
        purple = "#B19CD9"
        
        # Crear el eje X (recta real) desde -10 a 10
        number_line = NumberLine(
            x_range=[-10, 10, 1],
            length=12,
            color=cyan,
            include_numbers=True,
            label_direction=DOWN,
            font_size=24
        )
        number_line.move_to(ORIGIN)
        
        # Agregar título
        title = Text("Recta Real", font_size=36, color=cyan, weight=BOLD)
        title.to_edge(UP)
        
        # Crear línea de distancia desde 0 a 7
        distance_line = Line(
            start=number_line.number_to_point(0),
            end=number_line.number_to_point(7),
            color=purple,
            stroke_width=6
        )
        
        # Agregar puntos en 0 y 7
        point_0 = Dot(number_line.number_to_point(0), color=purple, radius=0.08)
        point_7 = Dot(number_line.number_to_point(7), color=purple, radius=0.08)
        
        # Etiqueta de distancia
        distance_label = Text("Distancia: 7", font_size=20, color=purple)
        distance_label.next_to(distance_line, UP, buff=0.3)
        
        # Agregar todos los elementos
        self.add(title)
        self.add(number_line)
        self.add(distance_line)
        self.add(point_0, point_7)
        self.add(distance_label)