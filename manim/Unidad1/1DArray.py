from manim import *

class ArregloUnidimensional(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"

        N = 10  # Cambia este valor si quieres más elementos
        arreglo_color = "#00FFFF"
        indices_color = WHITE
        etiquetas_color = "#B19CD9"  # Morado pastel
        
        # Título
        titulo = Text("Arreglo unidimensional", color=arreglo_color, font_size=40)
        titulo.to_edge(UP, buff=0.5)
        
        # Crear las celdas del arreglo
        arreglo = VGroup()
        for i in range(N):
            rect = Square(side_length=1, color=arreglo_color)
            if i == N-2:
                texto = MathTex(r"\dots", color=arreglo_color, font_size=36)
            elif i == N-1:
                texto = MathTex(r"a_{N}", color=arreglo_color, font_size=36)
            else:
                texto = MathTex(f"a_{{{i+1}}}", color=arreglo_color, font_size=36)
            texto.move_to(rect.get_center())
            cell = VGroup(rect, texto)
            arreglo.add(cell)

        arreglo.arrange(RIGHT, buff=0.2)
        arreglo.move_to(DOWN * 0.5)

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

        # Crear las etiquetas arriba del arreglo
        nombres = [
            "Primero", "Segundo", "Tercero", "Cuarto", "Quinto",
            "Sexto", "Séptimo", "Octavo", "...", "N-ésimo"
        ]
        etiquetas = VGroup()
        for i in range(N):
            nombre = nombres[i] if i < len(nombres) else "Enésimo"
            etiqueta = Text(nombre, color=etiquetas_color, font_size=24)
            etiqueta.rotate(3 * PI / 2)  # 270 grados
            etiqueta.next_to(arreglo[i], UP, buff=0.2)
            etiquetas.add(etiqueta)

        # Mostrar en la escena
        self.add(titulo, etiquetas, arreglo, indices)
