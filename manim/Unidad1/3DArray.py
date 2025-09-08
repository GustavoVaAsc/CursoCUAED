from manim import *
import random

class ArregloVerticalToArreglo3D(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"
        arreglo_color = "#00FFFF"
        flecha_color = "#B19CD9"
        texto_color = "#00FFFF"
        indice_color = WHITE

        # Configuración
        total_valores = 24  # 4x3x2 = 24
        random.seed(42)
        valores = random.sample(range(10, 100), total_valores)

        # Crear arreglo vertical con corte "..."
        arreglo_vertical = VGroup()
        valores_vertical = []
        direcciones_memoria = []
        base_address = 0xA000
        for i in range(total_valores):
            if i < 7:
                val = valores[i]
                valores_vertical.append(val)
                box = Rectangle(width=1.2, height=0.4, color=arreglo_color)
                value = Text(str(val), color=WHITE).scale(0.4)
                value.move_to(box.get_center())
                group = VGroup(box, value)
                arreglo_vertical.add(group)
            elif i == 7:
                valores_vertical.append("...")
                box = Rectangle(width=1.2, height=0.4, color=arreglo_color)
                value = Text("...", color=WHITE).scale(0.4)
                value.move_to(box.get_center())
                group = VGroup(box, value)
                arreglo_vertical.add(group)
            elif i >= 17:
                val = valores[i]
                valores_vertical.append(val)
                box = Rectangle(width=1.2, height=0.4, color=arreglo_color)
                value = Text(str(val), color=WHITE).scale(0.4)
                value.move_to(box.get_center())
                group = VGroup(box, value)
                arreglo_vertical.add(group)

        arreglo_vertical.arrange(DOWN, buff=0.04)
        arreglo_vertical.move_to(LEFT * 4)

        # Direcciones de memoria simuladas
        for i in range(total_valores):
            direcciones_memoria.append(f"0x{base_address + i * 4:04X}")

        # Etiquetas de direcciones de memoria a la izquierda
        arreglo_vertical_indices = VGroup()
        current_index = 0
        for i, box in enumerate(arreglo_vertical):
            if i == 7:
                idx = Text("", color=indice_color).scale(0.3)
            else:
                memoria_idx = i if i < 7 else i + 9
                idx = Text(direcciones_memoria[memoria_idx], color=indice_color).scale(0.3)
            idx.next_to(box, LEFT, buff=0.6)
            arreglo_vertical_indices.add(idx)
            current_index += 1

        # Etiquetas para las columnas
        indices_label_vertical = Text("Direcciones \nde memoria", color=texto_color, weight=BOLD).scale(0.32)
        datos_label_vertical = Text("       Datos \nen memoria", color=texto_color, weight=BOLD).scale(0.32)

        arreglo_vertical_group = VGroup(arreglo_vertical_indices, arreglo_vertical)
        arreglo_vertical_total = VGroup(indices_label_vertical, datos_label_vertical, arreglo_vertical_group)
        arreglo_vertical_total.arrange(RIGHT, buff=0.3)
        arreglo_vertical_total.move_to(LEFT * 5)

        indices_label_vertical.next_to(arreglo_vertical_indices, UP, buff=0.36)
        datos_label_vertical.next_to(arreglo_vertical, UP, buff=0.2)

        # Crear arreglo tridimensional 4x3x2
        arreglo_3d = VGroup()
        valor_idx = 0

        for k in range(2):  # profundidad
            plano = VGroup()
            for i in range(4):  # filas
                fila = VGroup()
                for j in range(3):  # columnas
                    rect = Rectangle(width=0.8, height=0.5, color=arreglo_color, fill_opacity=1)
                    opacity = 1.0 if k == 0 else 0.3
                    rect.set_fill(arreglo_color, opacity=opacity)
                    rect.set_z_index(-k)
                    group = VGroup(rect)
                    if k == 0:
                        val = valores[valor_idx]
                        text = Text(str(val), color="#0A192F", weight=BOLD).scale(0.5)
                        text.move_to(rect.get_center())
                        text.set_z_index(1)
                        group.add(text)
                    fila.add(group)
                    valor_idx += 1
                fila.arrange(RIGHT, buff=0.06)
                plano.add(fila)
            plano.arrange(DOWN, buff=0.06)
            plano.shift(RIGHT * k * 1.2 + UP * k * 0.3 + OUT * k * 0.5)

            if k == 0:
                plano.shift(RIGHT * 2.0)
            arreglo_3d.add(plano)

        # Etiqueta de nombre y flechas
        nombre_label = Text("nombre", color=indice_color, weight=BOLD).scale(0.35)
        nombre_label.next_to(datos_label_vertical, RIGHT, buff=1.0)

        flecha_nombre = CurvedArrow(
            start_point=nombre_label.get_bottom(),
            end_point=arreglo_vertical[0].get_right() + RIGHT * 0.2,
            color=flecha_color,
            stroke_width=2,
            angle=-PI / 2
        )

        flecha_conversion = Arrow(
            start=arreglo_3d.get_left() + LEFT * 0.2 + DOWN * 0.15,
            end=arreglo_vertical.get_right() + RIGHT * 0.2,
            color=flecha_color,
            stroke_width=15,
            max_stroke_width_to_length_ratio= 10,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )

        # Nota aclaratoria en la esquina inferior izquierda
        nota_label = Text(
            "Nota: El compilador busca en tiempo de ejecución donde almacenar \nel arreglo de forma contigua, por lo que las direcciones de memoria \npueden variar en cada ejecución.",
            color=WHITE,
            weight=BOLD
        ).scale(0.3)
        nota_label.to_edge(DOWN+RIGHT, buff=0.5)

        # Agregar todo a la escena
        self.add(
            arreglo_vertical_total,
            arreglo_3d,
            flecha_conversion,
            nombre_label,
            flecha_nombre,
            nota_label
        )
