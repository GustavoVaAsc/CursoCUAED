from manim import *
import random

class ColaFigura(Scene):
    def construct(self):
        # Fondo
        self.camera.background_color = "#0A192F"

        # Título de la escena
        title = Text("Cola (queue)", font_size=36, color="#00FFFF", weight=BOLD)
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
            # Rectángulo principal
            rect = Rectangle(
                width=node_width,
                height=node_height,
                fill_color=cyan,
                fill_opacity=0.7,
                stroke_color=cyan
            )
            # Calcular la posición x de la división (60% del ancho desde la izquierda)
            left_x = rect.get_left()[0]
            division_x = left_x + 0.6 * node_width

            # Línea divisoria vertical (se extiende desde el tope al fondo del rectángulo)
            divider = Line(
                start=[division_x, rect.get_top()[1], 0],
                end=[division_x, rect.get_bottom()[1], 0],
                color=cyan
            )
            # Agrupar el rectángulo y la división
            node = VGroup(rect, divider)
            nodes_list.append(node)
        nodes = VGroup(*nodes_list)
        nodes.arrange(RIGHT, buff=node_spacing)
        nodes.move_to(ORIGIN)

        # Etiquetas para los nodos: color morado y posicionadas a la izquierda de la línea divisoria
        labels = VGroup()
        for node in nodes:
            # Generar texto aleatorio: K{número aleatorio}
            num = random.randint(1, 100)
            label = Text(f"K{num}", font_size=20, color="#871F78")

            # Obtener la posición x de la línea divisoria del nodo:
            # Se usa el rectángulo (primer submobject) del grupo para calcularlo
            division_x = node[0].get_left()[0] + 0.6 * node_width
            center_y = node[0].get_center()[1]
            
            # Posicionar la etiqueta a la izquierda de la división, adherida a su borde derecho
            # Usamos un Dot invisible como referencia de posición
            divider_ref = Dot([division_x, center_y, 0])
            label.next_to(divider_ref, LEFT, buff=0.05)
            labels.add(label)

        # Flechas que indican los apuntadores entre nodos (4 flechas para 5 nodos)
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
            arrow.tip.scale(1.5)  # aumentar el tamaño de la punta

        self.add(nodes, arrows, labels)

        # Etiquetas para indicar el Head y el Tail de la cola, cada una con una flecha sumada al texto
        head_text = Text("Head", font_size=20, color=morado)
        head_arrow_icon = Arrow(ORIGIN, DOWN, buff=0, color=morado, stroke_width=8).scale(1)
        head_group = VGroup(head_text, head_arrow_icon).arrange(DOWN)
        head_group.next_to(nodes[0], UP)

        tail_text = Text("Tail", font_size=20, color=morado)
        tail_arrow_icon = Arrow(ORIGIN, DOWN, buff=0, color=morado, stroke_width=8).scale(1)
        tail_group = VGroup(tail_text, tail_arrow_icon).arrange(DOWN)
        tail_group.next_to(nodes[-1], UP)

        self.add(head_group, tail_group)
