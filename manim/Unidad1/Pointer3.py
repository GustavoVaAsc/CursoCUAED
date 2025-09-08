from manim import *

class PunteroAArreglo(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"
        arreglo = [77, 66, 55, 44, 33, 22, 11, 9]
        arreglo_color = "#00FFFF"
        flecha_color = "#B19CD9"
        texto_color = "#00FFFF"
        direcciones_memoria = ["0xA08", "0xA09", "0xA0A", "0xA0B", "0xA0C", "0xA0D","0xA0E","0xA0F"]  # Direcciones de memoria en hexadecimal

        # Crear cajas verticales
        vertical_boxes = VGroup()
        index_labels = VGroup()
        for i, val in enumerate(arreglo):
            box = Rectangle(width=1.7, height=0.6, color=arreglo_color)
            if i == 7:
                value = Text('0xA09', color=WHITE).scale(0.4)
                value.move_to(box.get_center())
                group = VGroup(box, value)
                vertical_boxes.add(group)
            else:
                group = VGroup(box)
                vertical_boxes.add(group)

            idx = Text(direcciones_memoria[i], color=WHITE).scale(0.4)  
            index_labels.add(idx)

        # Arreglar verticalmente con menos separación
        vertical_boxes.arrange(DOWN, buff=0.05)
        vertical_boxes.move_to(LEFT)
        
        elements = VGroup()
        for i in range(5):
            elements.add(VGroup(Text('arr['+str(i)+']',color=flecha_color).scale(0.4)))
        elements.add(VGroup(Text('apEnt', color=flecha_color).scale(0.4)))

        # Posicionar índices junto a cada caja
        for i, group in enumerate(vertical_boxes):
            if i>=1 and i<=5:
                elements[i-1].next_to(group,LEFT,buff=0.3)
            elif i==7:
                elements[5].next_to(group, LEFT, buff=0.3)
                
            index_labels[i].next_to(group, RIGHT, buff=0.3)

        # Flecha curva desde "nombre"
        flecha_nombre = CurvedArrow(
            start_point=index_labels[7].get_right(),
            end_point=index_labels[1].get_right() + UP * 0.05,
            color=flecha_color,
            stroke_width=4,
            angle=PI
        )

        # Agregar todos los elementos a la escena
        self.add(vertical_boxes, elements,index_labels,
                flecha_nombre)
