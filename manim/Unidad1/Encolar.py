from manim import *
import random

class Encolar(Scene):
    def construct(self):
        # Fondo
        self.camera.background_color = "#0A192F"

        # Título de la escena
        title = Text("Encolar", font_size=36, color="#00FFFF", weight=BOLD)
        title.to_edge(UP)
        self.add(title)

        # Colores
        cyan = "#00FFFF"
        morado = "#B19CD9"

        # Dimensiones y espaciado
        node_width = 1.5
        node_height = 0.75
        node_spacing = 0.5

        # Crear 4 nodos iniciales de la cola usando rectángulos con división interna
        nodes_list = []
        for i in range(4):
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
            # Ubicar la etiqueta a la izquierda de la línea divisoria
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
            for i in range(len(nodes_list) - 1)
        ])
        for arrow in arrows:
            arrow.tip.scale(1.5)

        # Apuntador Tail (estático, inicialmente en el último nodo)
        tail_text = Text("Tail", font_size=20, color=morado)
        tail_arrow_icon = Arrow(ORIGIN, DOWN, buff=0, color=morado, stroke_width=8)
        tail_group = VGroup(tail_text, tail_arrow_icon).arrange(DOWN)
        tail_group.next_to(nodes[-1], UP)

        # Apuntador Head (estático en el primer nodo, paralelo a Tail)
        head_text = Text("Head", font_size=20, color=morado)
        head_arrow_icon = Arrow(ORIGIN, DOWN, buff=0, color=morado, stroke_width=8)
        head_group = VGroup(head_text, head_arrow_icon).arrange(DOWN)
        head_group.next_to(nodes[0], UP)
        # El updater mantiene el apuntador pegado al primer nodo aunque éste se mueva
        head_group.add_updater(lambda m: m.next_to(nodes[0], UP))

        self.add(nodes, labels, arrows, tail_group, head_group)
        self.wait(1)

        # ---------- Animación de encolar ----------

        # Crear el nuevo nodo a encolar (elemento a la derecha de la cola)
        new_rect = Rectangle(
            width=node_width,
            height=node_height,
            fill_color=cyan,
            fill_opacity=0.7,
            stroke_color=cyan
        )
        new_left_x = new_rect.get_left()[0]
        new_division_x = new_left_x + 0.6 * node_width
        new_divider = Line(
            start=[new_division_x, new_rect.get_top()[1], 0],
            end=[new_division_x, new_rect.get_bottom()[1], 0],
            color=cyan
        )
        new_node = VGroup(new_rect, new_divider)
        # Etiqueta para el nuevo nodo
        new_num = random.randint(1, 100)
        new_label = Text(f"K{new_num}", font_size=20, color="#871F78")
        new_divider_ref = Dot([new_division_x, new_rect.get_center()[1], 0], radius=0.001, color=BLACK)
        new_label.next_to(new_divider_ref, LEFT, buff=0.05)
        # Grupo del nuevo nodo (conteniendo nodo y etiqueta)
        new_group = VGroup(new_node, new_label)

        # Posición final del nuevo nodo: a la derecha del último nodo de la cola
        final_new_node_position = nodes[-1].get_right() + RIGHT * (node_spacing + node_width/2)
        new_group.move_to(final_new_node_position)

        # Flecha que conectará el antiguo tail con el nuevo nodo
        new_arrow = Arrow(
            start=nodes[-1].get_right(),
            end=new_node.get_left(),
            buff=0.1,
            color=morado,
            stroke_width=50,
            max_stroke_width_to_length_ratio=10,
        ).scale(1.5)
        new_arrow.tip.scale(1.5)
        new_arrow.set_opacity(1)

        # Animar la aparición del nuevo nodo
        self.play(FadeIn(new_group))
        self.wait(0.5)

        # Mostrar la flecha
        self.play(FadeIn(new_arrow))
        self.wait(0.5)

        # Mover el apuntador Tail al nuevo nodo
        tail_group.generate_target()
        tail_group.target.next_to(new_group, UP)
        self.play(MoveToTarget(tail_group))
        self.wait(1)

        # Mover ligeramente todos los elementos a la izquierda (head_group se mantiene actualizado)
        shift_distance = LEFT * 0.6
        self.play(
            nodes.animate.shift(shift_distance),
            labels.animate.shift(shift_distance),
            arrows.animate.shift(shift_distance),
            tail_group.animate.shift(shift_distance),
            new_group.animate.shift(shift_distance),
            new_arrow.animate.shift(shift_distance)
        )
        self.wait(1)
