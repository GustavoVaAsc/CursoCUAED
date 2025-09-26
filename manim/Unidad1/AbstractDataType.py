from manim import *

class TipoDeDatoAbstracto(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"
        arreglo_color = "#00FFFF"
        flecha_color = "#B19CD9"
        texto_color = "#00FFFF"

        # Agregar título
        title = Text("Tipo de dato abstracto", font_size=36, color=texto_color, weight=BOLD).to_edge(UP)
        self.add(title)

        struct_code = '''<span fgcolor="#B19CD9">struct</span> <span fgcolor="#00FFFF">Producto</span><span fgcolor="#FFFFFF"> {</span>
    <span fgcolor="#B19CD9">int</span> <span fgcolor="#FFFFFF">cantidad</span>;
    <span fgcolor="#B19CD9">char</span> <span fgcolor="#FFFFFF">codigo</span>[5];
    <span fgcolor="#B19CD9">float</span> <span fgcolor="#FFFFFF">precio</span>;
};'''
        struct_text = MarkupText(struct_code, font="Source Code Pro", font_size=32).to_edge(LEFT).shift(RIGHT * 0.5)

        memory_blocks = VGroup()
        labels = [
            ("cantidad", 4, arreglo_color),
            ("codigo[0]", 1, flecha_color),
            ("codigo[1]", 1, flecha_color),
            ("codigo[2]", 1, flecha_color),
            ("codigo[3]", 1, flecha_color),
            ("codigo[4]", 1, flecha_color),
            ("precio", 4, arreglo_color),
        ]
        y_offset = 0.7
        block_height = 0.4
        block_width = 1.2
        memory_offset = 15  

        for label, size, color in labels:
            for i in range(size):
                rect = Rectangle(
                    height=block_height,
                    width=block_width,
                    stroke_color=color,
                    stroke_width=2
                ).shift(RIGHT * 3 + UP * (3.2 - y_offset))
                hex_text = Text(f"{memory_offset:#04X}", font_size=16, color="#FFFFFF").next_to(rect, RIGHT, buff=0.1)
                if i == 0:
                    left_text = Text(label, font_size=20, color=color).next_to(rect, LEFT, buff=0.1)
                    memory_blocks.add(VGroup(rect, left_text, hex_text))
                else:
                    memory_blocks.add(VGroup(rect, hex_text))
                y_offset += block_height
                memory_offset += 1

        memory_group = VGroup(*memory_blocks)
        memory_group.shift(DOWN * 0.5) 

        mem_title = Tex(r"\vdots", font_size=24, color=WHITE)
        mem_title.next_to(memory_group, UP, buff=0.2)
        
        boxes = VGroup(*[group[0] for group in memory_group.submobjects if len(group) > 0])
        mem_title.move_to(np.array([boxes.get_center()[0], mem_title.get_center()[1], 0]))
        mem_down = Tex(r"\vdots", font_size=24, color=WHITE)
        mem_down.next_to(memory_group,DOWN, buff = 0.2)
        mem_down.move_to(np.array([boxes.get_center()[0], mem_down.get_center()[1], 0]))
        nota_text = Text(
            "Nota: cada bloque representa 1 byte. \nchar = 1 byte \nint = 4 bytes \nfloat = 4 bytes",
            font_size=18,
            color=WHITE
        ).next_to(struct_text, DOWN, buff=0.5)
        self.add(nota_text)
        self.add(struct_text)
        self.add(memory_group)
        self.add(mem_title)
        self.add(mem_down)
        
        # Agregar llave "}" que abarca todos los bloques de la memoria con la etiqueta "Producto"
        bracket = Brace(memory_group, RIGHT, buff=0.2, color=texto_color)  
        bracket_label = Text("Producto", font_size=24, color=texto_color).move_to(bracket.get_right()).shift(RIGHT)
        self.add(bracket, bracket_label)