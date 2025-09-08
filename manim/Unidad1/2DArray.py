from manim import *

class MatrizToArreglo(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"
        arreglo_color = "#00FFFF"
        flecha_color = "#B19CD9"
        texto_color = "#00FFFF"
        indice_color = WHITE  # Color blanco para los índices

        # Crear matriz 2D
        matriz = VGroup()
        valor = 1
        for i in range(4):  # filas
            fila = VGroup()
            for j in range(3):  # columnas
                box = Rectangle(width=0.8, height=0.5, color=arreglo_color)
                value = Text(str(valor), color=texto_color).scale(0.45)
                value.move_to(box.get_center())
                group = VGroup(box, value)
                fila.add(group)
                valor += 1
            fila.arrange(RIGHT, buff=0.06)
            matriz.add(fila)

        matriz.arrange(DOWN, buff=0.06)
        matriz.move_to(LEFT * 3.5)

        # Crear índices de columnas (arriba de la matriz)
        indices_columnas = VGroup()
        for j in range(3):
            idx = Text(str(j), color=indice_color).scale(0.4)
            idx.next_to(matriz[0][j], UP, buff=0.3)
            indices_columnas.add(idx)

        # Crear índices de filas (izquierda de la matriz)
        indices_filas = VGroup()
        for i in range(4):
            idx = Text(str(i), color=indice_color).scale(0.4)
            idx.next_to(matriz[i][0], LEFT, buff=0.3)
            indices_filas.add(idx)

        # Crear arreglo unidimensional vertical
        arreglo = VGroup()
        for i in range(1, 13):
            box = Rectangle(width=0.8, height=0.5, color=arreglo_color)
            value = Text(str(i), color=WHITE).scale(0.45)
            value.move_to(box.get_center())
            group = VGroup(box, value)
            arreglo.add(group)

        arreglo.arrange(DOWN, buff=0.06)
        arreglo.move_to(RIGHT * 3)

        # Direcciones de memoria para el arreglo (iniciando en 0xA000)
        direcciones_memoria = []
        base_address = 0xA000
        for i in range(12):
            direcciones_memoria.append(f"0x{base_address + i * 4:04X}")

        # Crear etiquetas de direcciones de memoria (a la derecha del arreglo)
        arreglo_indices = VGroup()
        for i, box in enumerate(arreglo):
            idx = Text(direcciones_memoria[i], color=indice_color).scale(0.35)
            idx.next_to(box, RIGHT, buff=0.6)
            arreglo_indices.add(idx)

        # Etiqueta de direcciones de memoria
        indices_label_arreglo = Text("Direcciones \nde memoria", color=texto_color, weight=BOLD).scale(0.3)
        indices_label_arreglo.next_to(arreglo_indices, UP, buff=0.37)

        # Etiqueta del arreglo ("Datos")
        arreglo_label = Text("       Datos \nen memoria", color=texto_color, weight=BOLD).scale(0.3)
        arreglo_label.next_to(arreglo, UP, buff=0.2)

        # Etiqueta "nombre" arriba del arreglo
        nombre_label = Text("nombre", color=indice_color, weight=BOLD).scale(0.4)
        nombre_label.next_to(arreglo_label, LEFT, buff=0.8)

        # Flecha curva desde "nombre" al primer elemento del arreglo
        flecha_nombre = CurvedArrow(
            start_point=nombre_label.get_bottom(),
            end_point=arreglo[0].get_left() + LEFT * 0.2,
            color=flecha_color,
            stroke_width=2,
            angle=PI / 2
        )

        # Flecha normal que conecta la matriz al arreglo
        flecha_conversion = Arrow(
            start=matriz.get_right() + RIGHT * 0.3,
            end=arreglo.get_left() + LEFT * 0.3,
            color=flecha_color,
            max_stroke_width_to_length_ratio=10,
            stroke_width=10,
            buff=0.1
        )

        # Nota aclaratoria sobre las direcciones de memoria (abajo a la izquierda)
        nota_label = Text(
            "Nota: El compilador busca en tiempo de ejecución donde almacenar el arreglo de \nforma contigua, por lo que las direcciones de memoria pueden variar en cada ejecución.",
            color=WHITE,
            weight=BOLD
        ).scale(0.3)
        nota_label.to_edge(DOWN + LEFT, buff=0.5)

        self.add(
            matriz, indices_columnas, indices_filas,
            arreglo, arreglo_indices, arreglo_label, indices_label_arreglo,
            nombre_label, flecha_nombre,
            flecha_conversion, nota_label
        )
