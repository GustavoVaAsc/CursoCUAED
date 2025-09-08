from manim import *

class ArregloVerticalHorizontal(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"
        arreglo = [55, 44, 33, 22, 11]
        arreglo_color = "#00FFFF"
        flecha_color = "#B19CD9"
        texto_color = "#00FFFF"
        direcciones_memoria = ["0xA000", "0xA004", "0xA008", "0xA00C", "0xA010"]  # Direcciones de memoria en hexadecimal

        # Crear cajas verticales
        vertical_boxes = VGroup()
        index_labels = VGroup()
        for i, val in enumerate(arreglo):
            box = Rectangle(width=2.2, height=0.6, color=arreglo_color)
            value = Text(str(val), color=WHITE).scale(0.6)
            value.move_to(box.get_center())
            group = VGroup(box, value)
            vertical_boxes.add(group)

            idx = Text(direcciones_memoria[i], color=WHITE).scale(0.6)  # Usar direcciones de memoria en lugar de índices
            index_labels.add(idx)

        # Arreglar verticalmente con menos separación
        vertical_boxes.arrange(DOWN, buff=0.05)
        vertical_boxes.move_to(LEFT * 4)

        # Posicionar índices junto a cada caja
        for i, group in enumerate(vertical_boxes):
            index_labels[i].next_to(group, LEFT, buff=0.3)

        # Etiquetas
        memoria_label = Text("       Datos \nen memoria", color=texto_color, weight=BOLD).scale(0.4)
        memoria_label.next_to(vertical_boxes, UP, buff=0.3)

        indices_label = Text("Direcciones \n          de \n   memoria", color=texto_color, weight=BOLD).scale(0.4)  # Cambiado a direcciones de memoria
        indices_label.next_to(index_labels, UP, buff=0.3)

        nombres_label = Text("nombre", color=WHITE, weight=BOLD).scale(0.35)
        nombres_label.move_to(memoria_label.get_top() + RIGHT * 2.5)

        # Flecha curva desde "nombre"
        flecha_nombre = CurvedArrow(
            start_point=nombres_label.get_bottom(),
            end_point=vertical_boxes[0].get_right() + UP * 0.05,
            color=flecha_color,
            stroke_width=2,
            angle=-PI / 2
        )

        # Crear cajas horizontales
        horizontal_boxes = VGroup()
        for val in arreglo:
            box = Rectangle(width=1, height=0.6, color=arreglo_color)
            value = Text(str(val), color=texto_color).scale(0.6)
            value.move_to(box.get_center())
            group = VGroup(box, value)
            horizontal_boxes.add(group)

        horizontal_boxes.arrange(RIGHT, buff=0.1)
        horizontal_boxes.move_to(RIGHT * 3)

        # Agregar índices encima del arreglo horizontal
        horizontal_index_labels = VGroup()
        for i in range(len(arreglo)):
            idx = Text(f"{i}", color=WHITE).scale(0.6)
            horizontal_index_labels.add(idx)

        # Posicionar los índices encima de las cajas horizontales
        for i, group in enumerate(horizontal_boxes):
            horizontal_index_labels[i].move_to(group.get_center() + UP * 0.6)

        flecha_conversion = Arrow(
            start=horizontal_boxes.get_left() + LEFT * 0.5,
            end=vertical_boxes.get_right() + RIGHT * 0.5,
            color=flecha_color,
            max_stroke_width_to_length_ratio= 10,
            stroke_width=50,
            buff=0.1
        )

        # Nota aclaratoria en la esquina inferior izquierda
        nota_label = Text(
            "Nota: El compilador busca en tiempo de ejecución donde almacenar el arreglo de forma contigua, por lo \nque las direcciones de memoria pueden variar en cada ejecución.",
            color=WHITE,
            weight=BOLD
        ).scale(0.3)
        nota_label.to_edge(DOWN + LEFT, buff=0.5)

        self.add(vertical_boxes, index_labels, memoria_label, indices_label,
                 nombres_label, flecha_nombre, horizontal_boxes, flecha_conversion, 
                 horizontal_index_labels, nota_label)
