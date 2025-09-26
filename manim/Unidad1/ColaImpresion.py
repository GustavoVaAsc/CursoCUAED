from manim import *
import random

class ColaImpresion(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"
        
        # Colores del archivo original
        cyan = "#00FFFF"
        purple = "#B19CD9"
        
        # Título
        title = Text("Cola de Impresión", font_size=36, color=cyan, weight=BOLD)
        title.to_edge(UP)
        self.add(title)
        
        # Crear impresora (imagen y etiqueta por separado)
        printer_img = ImageMobject("elements/ColaImpresion/printer.png")
        printer_img.scale_to_fit_width(2)
        printer_img.move_to(LEFT * 5)
        
        printer_label = Text("Impresora", font_size=16, color=purple)
        printer_label.next_to(printer_img, DOWN, buff=0.2)
        
        self.add(printer_img, printer_label)
        self.wait(1)
        
        # Listas para almacenar los elementos de la cola por separado
        document_images = []
        document_labels = []
        extensions = [".pdf", ".docx", ".png", ".jpg", ".txt", ".xlsx"]
        
        # Generar 6 elementos en la cola, uno por segundo
        for i in range(1, 7):
            # Crear documento (imagen)
            doc_img = ImageMobject("elements/ColaImpresion/document.png")
            doc_img.scale_to_fit_width(1)
            
            
            # Etiqueta del documento
            doc_label = Text(f"documento{i}{random.choice(extensions)}", font_size=12, color=cyan)
            
            # Posicionar elementos por separado
            base_position = printer_img.get_right() + RIGHT * 2 + RIGHT * (i-1) * 1.5
            doc_img.move_to(base_position)
            doc_label.next_to(doc_img, DOWN, buff=0.1)
            
            document_images.append(doc_img)
            document_labels.append(doc_label)
            
            # Animar la aparición del documento
            self.play(FadeIn(doc_img), FadeIn(doc_label))
            self.wait(1)
        
        self.wait(1)
        
        # Desencolar elementos uno por uno
        for i in range(len(document_images)):
            current_img = document_images[i]
            current_label = document_labels[i]
            
            # Mover el elemento hacia la impresora
            self.play(
                current_img.animate.move_to(printer_img.get_center()),
                current_label.animate.next_to(printer_img, DOWN, buff=0.2)
            )
            
            # Hacer que el elemento "desaparezca" en la impresora
            self.play(FadeOut(current_img), FadeOut(current_label))
            
            # Mover los elementos restantes hacia la izquierda
            remaining_images = document_images[i+1:]
            remaining_labels = document_labels[i+1:]
            
            if remaining_images:
                animations = []
                for j, (img, label) in enumerate(zip(remaining_images, remaining_labels)):
                    new_position = printer_img.get_right() + RIGHT * 2 + RIGHT * j * 1.5
                    animations.append(img.animate.move_to(new_position))
                    animations.append(label.animate.move_to(new_position + DOWN * 0.8))
                self.play(*animations)
            
            self.wait(1)