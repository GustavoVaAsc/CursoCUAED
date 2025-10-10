from manim import *

class ApilarDesapilar(Scene):
    def construct(self):
        # Fondo
        self.camera.background_color = "#0A192F"

        # Colores
        cyan = "#00FFFF"
        morado = "#B19CD9"

        # Dimensiones de los rectángulos
        rect_width = 2.5
        rect_height = 0.8
        spacing = 0.2

        # Crear 5 rectángulos apilados verticalmente en el centro
        stack_rects = VGroup()
        for i in range(5):
            rect = Rectangle(
                width=rect_width,
                height=rect_height,
                fill_color=cyan,
                fill_opacity=0.7,
                stroke_color=cyan
            )
            stack_rects.add(rect)
        
        stack_rects.arrange(DOWN, buff=spacing)
        stack_rects.move_to(ORIGIN+DOWN)

        # Rectángulo en esquina superior izquierda
        left_rect = Rectangle(
            width=rect_width,
            height=rect_height,
            fill_color=cyan,
            fill_opacity=0.7,
            stroke_color=cyan
        )
        left_rect.to_corner(UL, buff=1)

        # Rectángulo en esquina superior derecha
        right_rect = Rectangle(
            width=rect_width,
            height=rect_height,
            fill_color=cyan,
            fill_opacity=0.7,
            stroke_color=cyan
        )
        right_rect.to_corner(UR, buff=1)

        # Flecha curva desde rectángulo izquierdo hacia el tope de la pila
        arrow_apilar = CurvedArrow(
            start_point=left_rect.get_right(),
            end_point=stack_rects[0].get_top()+LEFT*0.4,
            color=morado,
            angle=-PI/2,
            stroke_width=6
        )

        # Flecha curva desde el tope de la pila hacia rectángulo derecho
        arrow_desapilar = CurvedArrow(
            start_point=stack_rects[0].get_top()+RIGHT*0.4,
            end_point=right_rect.get_left(),
            angle=-PI/2,
            color=morado,
            stroke_width=6
        )

        # Etiquetas para las operaciones
        label_apilar = Text("Apilar", font_size=22, color=morado, weight=BOLD)
        label_apilar.next_to(arrow_apilar, DOWN+UP*1, buff=0.05)

        label_desapilar = Text("Desapilar", font_size=22, color=morado, weight=BOLD)
        label_desapilar.next_to(arrow_desapilar, DOWN+UP*1, buff=0.05)

        # Agregar todos los elementos a la escena
        self.add(stack_rects, left_rect, right_rect)
        self.add(arrow_apilar, arrow_desapilar)
        self.add(label_apilar, label_desapilar)