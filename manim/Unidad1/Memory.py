from manim import *

class RegionesMemoria(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"

        # Agregar título a la escena
        title = Text("Regiones de memoria", font_size=36, color="#00FFFF", weight=BOLD)
        title.to_edge(UP)
        self.add(title)

        # Definir el contenedor total de memoria (vertical)
        total_memory = Rectangle(
            height=6,
            width=2,
            fill_color=WHITE,
            fill_opacity=0.2,
            stroke_color=WHITE
        )
        total_memory.move_to(ORIGIN + LEFT*0.8+DOWN*0.5)

        # Definir los colores para stack y heap
        cyan = "#00FFFF"      # Stack
        purple = "#B19CD9"    # Heap

        # Alturas fijas para Stack y Heap
        stack_height = 1.3
        heap_height = 1.3
        empty_height = total_memory.height - (stack_height + heap_height)

        # Crear el rectángulo de la stack (parte superior = memoria alta)
        stack = Rectangle(
            height=stack_height,
            width=total_memory.width,
            fill_color=cyan,
            fill_opacity=1,
            stroke_color=cyan
        )
        # Crear un rectángulo que representa el espacio vacío (expandible)
        empty_space = Rectangle(
            height=empty_height,
            width=total_memory.width,
            fill_color=BLACK,
            fill_opacity=0,
            stroke_color=WHITE,
            stroke_opacity=0.5
        )
        # Crear el rectángulo del heap (parte inferior = memoria baja)
        heap = Rectangle(
            height=heap_height,
            width=total_memory.width,
            fill_color=purple,
            fill_opacity=1,
            stroke_color=purple
        )

        # Agrupar las regiones verticalmente (arrange de arriba hacia abajo)
        memory_regions = VGroup(stack, empty_space, heap)
        memory_regions.arrange(DOWN, buff=0)
        memory_regions.move_to(total_memory.get_center())

        # Etiquetas para cada sección interna
        label_stack = Text("Stack", font_size=20, color=BLACK).move_to(stack.get_center())
        label_heap = Text("Heap", font_size=20, color=BLACK).move_to(heap.get_center())

        # Agregar etiquetas de memoria alta y baja al contenedor total
        label_high = Text("Direcciones altas", font_size=22, color=cyan)
        label_low = Text("Direcciones bajas", font_size=22, color=cyan)
        label_high.next_to(total_memory.get_top(), (DOWN*0.2)+LEFT, buff=1.5)
        label_low.next_to(total_memory.get_bottom(), (UP*0.2)+LEFT, buff=1.5)

        # Crear el bloque de variables globales y estáticas de color rosa
        global_static = Rectangle(
            height=1.3,
            width=2,
            fill_color="#FF69C4",
            fill_opacity=1,
            stroke_color="#FF69C4"
        )
        label_global = Text(" Variables \n  globales \ny estáticas", font_size=20, color=BLACK).move_to(global_static.get_center())
        # Calcular la nueva altura del espacio vacío para incluir el bloque global_static
        global_static_height = global_static.height
        new_empty_height = total_memory.height - (stack_height + heap_height + global_static_height)
        empty_space.stretch_to_fit_height(new_empty_height)

        # Reagrupar las regiones de memoria de arriba hacia abajo: stack, espacio vacío, heap y global_static
        memory_regions = VGroup(stack, empty_space, heap, global_static)
        memory_regions.arrange(DOWN, buff=0)
        memory_regions.move_to(total_memory.get_center())

        # Reposicionar las etiquetas en el centro de cada bloque
        label_stack.move_to(stack.get_center())
        label_heap.move_to(heap.get_center())
        label_global.move_to(global_static.get_center())

        # Crear flecha desde el heap apuntando hacia arriba
        arrow_heap = Arrow(
            start=heap.get_top(),
            end=heap.get_top() + UP,
            buff=0,
            color=WHITE
        )

        # Crear flecha desde el stack apuntando hacia abajo
        arrow_stack = Arrow(
            start=stack.get_bottom(),
            end=stack.get_bottom() + DOWN,
            buff=0,
            color=WHITE
        )

        # Nota que especifica que el heap y el stack se pueden redimensionar
        nota = Text("Las flechas indican \nque el heap y el stack \nse pueden redimensionar", font_size=20, color=WHITE)
        nota.next_to(empty_space, RIGHT, buff=1)

        # Agregar todos los elementos a la escena
        self.add(total_memory, memory_regions, label_stack, label_heap, label_high, label_low,
                 global_static, label_global, arrow_heap, arrow_stack, nota)
