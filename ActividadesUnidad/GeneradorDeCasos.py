import random
import string

def generar_testcase_satelite():
    longitud = random.randint(5, 200)
    
    costo = round(random.uniform(5.0, 1000.0), 2)
    
    # Probabilidad de que un caracter sea ruido (#)
    # Un 30% de probabilidad de ruido hace casos interesantes
    probabilidad_ruido = 0.3 
    
    caracteres_validos = string.ascii_letters + string.digits + " " 
    mensaje_lista = []
    
    for _ in range(longitud):
        if random.random() < probabilidad_ruido:
            mensaje_lista.append("#")
        else:
            mensaje_lista.append(random.choice(caracteres_validos))
            
    # Convertimos la lista a string
    mensaje_sucio = "".join(mensaje_lista)
    
    if "#" not in mensaje_sucio:
        mid = len(mensaje_sucio) // 2
        mensaje_sucio = mensaje_sucio[:mid] + "#" + mensaje_sucio[mid:]

    cantidad_eliminados = mensaje_sucio.count("#")
    dinero_ahorrado = cantidad_eliminados * costo
    mensaje_limpio = mensaje_sucio.replace("#", "")

    c_test_code = f'char buffer[] = "{mensaje_sucio}";\n'
    c_test_code += f'limpiarTransmision(buffer, {costo:.2f});'

    expected_output = f"{cantidad_eliminados}\n"
    expected_output += f"{dinero_ahorrado:.2f}\n"
    expected_output += f"{mensaje_limpio}"

    return c_test_code, expected_output

if __name__ == "__main__":
    CANTIDAD_CASOS = 5 
    
    print("="*50)
    print(f"GENERADOR DE TESTS - SATELITEX ({CANTIDAD_CASOS} CASOS)")
    print("="*50)
    
    for i in range(1, CANTIDAD_CASOS + 1):
        codigo, salida = generar_testcase_satelite()
        
        print(f"\n--- TEST CASE {i} ---")
        print(">> TEST CODE:")
        print(codigo)
        print("-" * 20)
        print(">> EXPECTED OUTPUT:")
        print(salida)
        print("-" * 50)
