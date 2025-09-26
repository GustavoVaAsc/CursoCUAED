from manim import *
import random

class Desencolar(Scene):
    def construct(self):
        # Fondo
        self.camera.background_color = "#0A192F"

        # Título de la escena
        title = Text("Desencolar", font_size=36, color="#00FFFF", weight=BOLD)
        title.to_edge(UP)
        self.add(title)

        # Colores
        cyan = "#00FFFF"
        morado = "#B19CD9"

        # Dimensiones y espaciado
        node_width = 1.5
        node_height = 0.75
        node_spacing = 0.5

        # Crear 5 nodos de la cola usando rectángulos con división interna
        nodes_list = []
        for i in range(5):
            rect = Rectangle(
                width=node_width,
                height=node_height,
                fill_color=cyan,
                fill_opacity=0.7,
                stroke_color=cyan
            )
            left_x = rect.get_left()[0]
            division_x = left_x + 0.6 * node_width
            divider = Line(
                start=[division_x, rect.get_top()[1], 0],
                end=[division_x, rect.get_bottom()[1], 0],
                color=cyan
            )
            node = VGroup(rect, divider)
            nodes_list.append(node)
        nodes = VGroup(*nodes_list)
        nodes.arrange(RIGHT, buff=node_spacing)
        nodes.move_to(ORIGIN)

        # Etiquetas para los nodos
        labels = VGroup()
        for node in nodes:
            num = random.randint(1, 100)
            label = Text(f"K{num}", font_size=20, color="#871F78")
            division_x = node[0].get_left()[0] + 0.6 * node_width
            center_y = node[0].get_center()[1]
            divider_ref = Dot([division_x, center_y, 0], radius=0.001, color=BLACK)
            label.next_to(divider_ref, LEFT, buff=0.05)
            labels.add(label)

        # Flechas que conectan los nodos
        arrows = VGroup(*[
            Arrow(
                start=nodes[i].get_right(),
                end=nodes[i+1].get_left(),
                buff=0.1,
                color=morado,
                stroke_width=50,
                max_stroke_width_to_length_ratio=10,
            ).scale(1.5)
            for i in range(4)
        ])
        for arrow in arrows:
            arrow.tip.scale(1.5)

        # Apuntador Head (único, ya que desencolamos desde el inicio)
        head_text = Text("Head", font_size=20, color=morado)
        head_arrow_icon = Arrow(ORIGIN, DOWN, buff=0, color=morado, stroke_width=8)
        head_group = VGroup(head_text, head_arrow_icon).arrange(DOWN)
        head_group.next_to(nodes[0], UP)

        # Apuntador Tail (estático, permanece en el último nodo)
        tail_text = Text("Tail", font_size=20, color=morado)
        tail_arrow_icon = Arrow(ORIGIN, DOWN, buff=0, color=morado, stroke_width=8)
        tail_group = VGroup(tail_text, tail_arrow_icon).arrange(DOWN)
        tail_group.next_to(nodes[-1], UP)

        self.add(nodes, labels, arrows, head_group, tail_group)
        self.wait(1)

        # ---------- Animación de desencolado ----------

        # 1. Resaltar el primer nodo (Head)
        first_node = nodes[0]
        self.play(Indicate(first_node, color="#39ff14", scale_factor=1.2))
        self.wait(0.5)

        # 2. Eliminar la flecha que conecta el primer nodo con el siguiente
        first_arrow = arrows[0]
        self.play(FadeOut(first_arrow))
        self.wait(0.5)

        # 3. Animar la salida del primer nodo y desaparecer su etiqueta simultáneamente
        first_label = labels[0]
        self.play(
            first_node.animate.shift(LEFT * 2 + DOWN * 2),
            FadeOut(first_node, shift=LEFT * 2 + DOWN * 2),
            FadeOut(first_label)
        )
        self.wait(0.5)

        # 4. Animar el movimiento del apuntador Head hacia el siguiente nodo (nuevo head)
        new_head = nodes[1]
        head_group.generate_target()
        head_group.target.next_to(new_head, UP)
        self.play(MoveToTarget(head_group))
        self.wait(1)
