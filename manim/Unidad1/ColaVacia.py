from manim import *

class ColaVacia(Scene):
    def construct(self):
        # Configuración de colores de la escena original
        background_color = "#0A192F"
        text_color = "#00FFFF"
        arrow_color = "#B19CD9"
        self.camera.background_color = background_color

        # Crear título "Cola vacía"
        title = Text("Cola vacía", color=text_color, weight=BOLD).scale(0.8)
        title.to_edge(UP)

        # Crear etiqueta "NULL" y moverla al centro
        null_label = Text("NULL", color=text_color).scale(0.6)
        null_label.move_to(ORIGIN)

        # Crear etiquetas para punteros "Head" y "Tail"
        head_label = Text("Head", color=arrow_color).scale(0.5)
        tail_label = Text("Tail", color=arrow_color).scale(0.5)

        # Posicionar "Head" a la izquierda y "Tail" a la derecha de "NULL"
        head_label.next_to(null_label, LEFT + (UP*0.5), buff=2)
        tail_label.next_to(null_label, RIGHT + (UP*0.5), buff=2)

        # Crear flechas que apunten desde los punteros hacia "NULL"
        head_arrow = Arrow(
            start=head_label.get_right(),
            end=null_label.get_left(),
            color=arrow_color,
            buff=0.1,
            stroke_width=4
        )
        tail_arrow = Arrow(
            start=tail_label.get_left(),
            end=null_label.get_right(),
            color=arrow_color,
            buff=0.1,
            stroke_width=4
        )

        # Agregar todos los elementos a la escena
        self.add(title, null_label, head_label, tail_label, head_arrow, tail_arrow)
