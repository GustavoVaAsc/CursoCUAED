from manim import *

class EstructuraLineal(Scene):
    def construct(self):
        # Fondo
        self.camera.background_color = "#0A192F"

        # Título de la escena
        title = Text("Estructura de Datos Lineal", font_size=36, color="#00FFFF", weight=BOLD)
        title.to_edge(UP)
        self.add(title)

        # Colores
        cyan = "#00FFFF"
        morado = "#B19CD9"
        verde_neon = "#00FF00"

        # Dimensiones y espaciado (escalado)
        node_width = 2.0
        node_height = 1.0
        node_spacing = 0.8

        # Crear 3 nodos de la estructura usando rectángulos con división interna
        nodes_list = []
        for i in range(3):
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

        # Flechas que indican los apuntadores entre nodos (2 flechas para 3 nodos)
        arrows = VGroup(*[
            Arrow(
                start=nodes[i].get_right(),
                end=nodes[i+1].get_left(),
                buff=0.1,
                color=morado,
                stroke_width=50,
                max_stroke_width_to_length_ratio=10,
            ).scale(1.5)
            for i in range(2)
        ])
        for arrow in arrows:
            arrow.tip.scale(1.5)  # aumentar el tamaño de la punta

        self.add(nodes, arrows)

        # Cuadrado verde neón encerrando al elemento del medio
        middle_highlight = Rectangle(
            width=node_width + 0.3,
            height=node_height + 0.3,
            stroke_color=verde_neon,
            stroke_width=6,
            fill_color=verde_neon,
            fill_opacity=0.2
        )
        middle_highlight.move_to(nodes[1].get_center())

        # Etiqueta "predecesor" encima del primer nodo
        predecessor_text = Text("Predecesor", font_size=24, color="WHITE")
        predecessor_text.next_to(nodes[0], UP, buff=1.2)
        predecessor_arrow = Arrow(
            start=predecessor_text.get_bottom(),
            end=nodes[0].get_top(),
            color="WHITE",
            stroke_width=23,
            max_stroke_width_to_length_ratio=15
        ).scale(1.3)
        predecessor_arrow.tip.scale(2.5)
        
        # Etiqueta "sucesor" encima del tercer nodo
        successor_text = Text("Sucesor", font_size=24, color="WHITE")
        successor_text.next_to(nodes[2], UP, buff=1.2)
        successor_arrow = Arrow(
            start=successor_text.get_bottom(),
            end=nodes[2].get_top(),
            color="WHITE",
            stroke_width=23,
            max_stroke_width_to_length_ratio=15
        ).scale(1.3)
        successor_arrow.tip.scale(2.5)

        # Etiqueta "actual" encima del nodo del medio
        actual_text = Text("Actual", font_size=24, color=verde_neon)
        actual_text.next_to(nodes[1], UP, buff=0.3)
        
        self.add(middle_highlight, predecessor_text, predecessor_arrow, successor_text, successor_arrow, actual_text)