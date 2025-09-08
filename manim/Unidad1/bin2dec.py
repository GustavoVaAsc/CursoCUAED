from manim import *

class DecimalToBinaryConversion(Scene):
    def construct(self):
        # Configuración del fondo
        self.camera.background_color = "#0A192F"
        
        # Título
        title = Text("Conversión de decimal a binario", font_size=36, color="#00FFFF")
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP, buff=0.5))
        
        # Número decimal a convertir
        decimal_number = 45
        number_text = MathTex(f"Decimal:  {decimal_number}", font_size=28)
        number_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(number_text))
        self.wait(1)
        
        # Proceso de conversión
        current_number = decimal_number
        binary_digits = []
        steps = VGroup()
        
        while current_number > 0:
            remainder = current_number % 2
            quotient = current_number // 2
            binary_digits.append(remainder)
            
            # Visualización de los cálculos
            step_text = MathTex(f"{current_number} \div 2 = {quotient}, \quad {current_number} \mod 2 = {remainder}", font_size=24)
            if steps:
                step_text.next_to(steps[-1], DOWN, buff=0.3)
            else:
                step_text.next_to(number_text, DOWN, buff=0.5)
            
            steps.add(step_text)
            self.play(Write(step_text))
            self.wait(0.5)
            
            current_number = quotient
        
        self.wait(1)
        
        # Mostrar resultado final
        binary_digits.reverse()
        binary_result = "".join(map(str, binary_digits))
        result_text = Text(f"Resultado en binario: {binary_result}", font_size=28, color="#00FF0A")
        result_text.next_to(steps, DOWN, buff=0.5)
        self.play(Write(result_text))
        self.wait(2)
        
        # Explicación final
        final_message = Text("Cada residuo forma el número binario, leído de abajo hacia arriba", font_size=22, color="#00FFFF")
        final_message.next_to(result_text, DOWN, buff=0.3)
        self.play(Write(final_message))
        self.wait(3)
        
        # Finalizar animación
        self.play(FadeOut(VGroup(title, number_text, steps, result_text, final_message)))

class BinaryToDecimal(Scene):
    def construct(self):
        # Configuración del fondo
        self.camera.background_color = "#0A192F"
        
        # Título
        title = Text("Conversión de binario a decimal", font_size=36, color="#00FFFF")
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP, buff=0.5))
        
        # Número binario de ejemplo
        binary_number = "1011"
        number_text = MathTex(f"Binario: {binary_number}", font_size=28)
        number_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(number_text))
        self.wait(1)
        
        # Crear dígitos binarios y exponentes
        binary_digits = [MathTex(digit) for digit in binary_number]
        exponents = [MathTex(f"2^{{{len(binary_number) - 1 - i}}}") for i in range(len(binary_number))]
        
        # Organizar los dígitos y exponentes
        binary_group = VGroup(*binary_digits).arrange(RIGHT, buff=0.5)
        exponent_group = VGroup(*exponents).arrange(RIGHT, buff=0.5).next_to(binary_group, UP)
        
        # Agregar dígitos y exponentes a la escena
        self.play(Write(binary_group), Write(exponent_group))
        self.wait(1)
        
        # Explicación del proceso de conversión
        contributions = []
        
        for i, digit in enumerate(binary_number):
            contribution = int(digit) * (2 ** (len(binary_number) - 1 - i))
            contributions.append(contribution)
            
            # Mostrar proceso de multiplicación
            equation = MathTex(f"{digit} \cdot 2^{{{len(binary_number) - 1 - i}}} = {contribution}")
            explanation = Text(f"El dígito {digit} multiplica 2 elevado a {len(binary_number) - 1 - i}", font_size=18, color="#00FFFF")
            equation.next_to(binary_group, DOWN * 2)
            explanation.next_to(equation, DOWN, buff=0.2)
            
            self.play(binary_digits[i].animate.set_color(YELLOW), exponents[i].animate.set_color(YELLOW))
            self.play(Write(equation), Write(explanation))
            self.wait(1)
            
            # Resetear colores y borrar ecuación y explicación
            self.play(binary_digits[i].animate.set_color(WHITE), exponents[i].animate.set_color(WHITE))
            self.play(FadeOut(equation, explanation))
        
        # Mostrar la suma final
        sum_equation = MathTex(
            " + ".join(map(str, contributions)) + f" = {sum(contributions)}"
        )
        sum_equation.next_to(binary_group, DOWN * 2)
        self.play(Write(sum_equation))
        self.wait(2)
