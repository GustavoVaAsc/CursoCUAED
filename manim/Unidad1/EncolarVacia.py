from manim import *

class EncolarVacia(Scene):
    def construct(self):
        # Configuración de colores y fondo
        background_color = "#0A192F"
        cyan = "#00FFFF"
        arrow_color = "#B19CD9"
        text_color = "#00FFFF"
        self.camera.background_color = background_color

        title = Text("Encolar cuando la estructura está vacía", color=text_color, weight=BOLD).scale(0.8)
        title.to_edge(UP)
        self.add(title)

        # Mostrar etiqueta "NULL" en el centro junto a los punteros Head y Tail
        null_label = Text("NULL", color=text_color).scale(0.8)
        null_label.move_to(ORIGIN)
        self.add(null_label)

        head_label = Text("Head", color=arrow_color).scale(0.5)
        tail_label = Text("Tail", color=arrow_color).scale(0.5)
        head_label.next_to(null_label, LEFT + UP * 0.5, buff=2)
        tail_label.next_to(null_label, RIGHT + UP * 0.5, buff=2)
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
        self.add(head_label, tail_label, head_arrow, tail_arrow)
        self.wait(1)

        node_width = 1.5
        node_height = 0.75
        new_rect = Rectangle(
            width=node_width,
            height=node_height,
            fill_color=cyan,
            fill_opacity=0.7,
            stroke_color=cyan
        )
        new_left_x = new_rect.get_left()[0]
        division_x = new_left_x + 0.6 * node_width
        divider = Line(
            start=[division_x, new_rect.get_top()[1], 0],
            end=[division_x, new_rect.get_bottom()[1], 0],
            color=cyan
        )
        new_node = VGroup(new_rect, divider)

        # Crear etiqueta para el nuevo nodo
        new_label = Text("K1", font_size=20, color="#871F78")
        divider_ref = Dot([division_x, new_rect.get_center()[1], 0], radius=0.001, color=BLACK)
        new_label.next_to(divider_ref, LEFT, buff=0.05)

        node_group = VGroup(new_node, new_label)
        node_group.move_to(null_label.get_center())

        # Animar la sustitución de "NULL" por el nuevo nodo, sin desaparecer las flechas
        self.play(FadeOut(null_label))
        self.wait(0.5)
        self.play(FadeIn(node_group))
        self.wait(2)
