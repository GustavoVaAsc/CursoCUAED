from manim import *
import random

class ArregloUnidimensional(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"

        N = 7
        arreglo_color = "#00FFFF"
        indices_color = WHITE
        etiquetas_color = "#B19CD9"

        # Título
        titulo = Text("Anatomía de un arreglo", color=arreglo_color, font_size=40)
        titulo.to_edge(UP, buff=0.5)

        # Crear las celdas del arreglo
        arreglo = VGroup()
        for i in range(N):
            if i == N-2:
                texto = MathTex(r"\dots", color=arreglo_color, font_size=36)
            else:
                r = random.randint(-20, 20)
                color = etiquetas_color if i == 0 or i == N - 1 else arreglo_color
                texto = MathTex(f"{r}", color=color, font_size=36)
            rect = Square(side_length=1, color=arreglo_color)
            texto.move_to(rect.get_center())
            cell = VGroup(rect, texto)
            arreglo.add(cell)

        arreglo.arrange(RIGHT, buff=0.2)
        arreglo.move_to(DOWN*0.1)

        # Nombre del arreglo "arr" con flecha más larga hacia "Nombre del arreglo"
        arr_label = MathTex(r"\texttt{arr}", color=arreglo_color, font_size=50)
        arr_label.next_to(arreglo[0], LEFT, buff=0.5)

        nombre_texto = Text("Nombre del arreglo", font_size=24, color=WHITE, line_spacing=0.8)
        nombre_texto.next_to(arr_label, DOWN, buff=1.67) 

        flecha_arr = Arrow(start=nombre_texto.get_top(), end=arr_label.get_bottom(), color=WHITE, buff=0.1)

        nombre_arr = VGroup(arr_label, flecha_arr, nombre_texto)

        # Crear los índices debajo del arreglo
        indices = VGroup()
        for i in range(N):
            if i == N-2:
                idx = MathTex(r"i=\dots", color=indices_color, font_size=28)
            elif i == N-1:
                idx = MathTex(r"i=N-1", color=indices_color, font_size=28)
            else:
                idx = MathTex(f"i={i}", color=indices_color, font_size=28)
            idx.next_to(arreglo[i], DOWN, buff=0.2)
            indices.add(idx)
        
        # Flechas al primer y último elemento
        flecha_primero = Arrow(start=arreglo[0].get_top() + UP , end=arreglo[0].get_top(), color=etiquetas_color)
        etiqueta_primero = Text("Primer elemento", font_size=20, color=etiquetas_color)
        etiqueta_primero.next_to(flecha_primero, UP)

        flecha_ultimo = Arrow(start=arreglo[-1].get_top() + UP , end=arreglo[-1].get_top(), color=etiquetas_color)
        etiqueta_ultimo = Text("N-ésimo elemento", font_size=20, color=etiquetas_color)
        etiqueta_ultimo.next_to(flecha_ultimo, UP)

        # Flechas a dos elementos cualquiera
        i1, i2 = 2, 4
        flecha_elem1 = Arrow(start=arreglo[i1].get_top() + UP, end=arreglo[i1].get_top(), color=WHITE)
        etiqueta_elem1 = Text("elemento", font_size=20, color=WHITE)
        etiqueta_elem1.next_to(flecha_elem1, UP)

        # Llave horizontal que abarca todos los índices
        llave_indices = MathTex(r"\underbrace{\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad}", color=WHITE)
        llave_indices.scale(1.1)
        llave_indices.next_to(indices, DOWN, buff=0.3)

        texto_llave = Text("índices", font_size=24, color=WHITE)
        texto_llave.next_to(llave_indices, DOWN, buff=0.1)

        # Mostrar todo
        self.add(
            titulo, arreglo, indices,
            nombre_arr,
            flecha_primero, etiqueta_primero,
            flecha_ultimo, etiqueta_ultimo,
            flecha_elem1, etiqueta_elem1,
            llave_indices, texto_llave
        )
