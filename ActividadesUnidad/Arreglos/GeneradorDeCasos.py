import random

def generar_testcase():
    num_panes = random.randint(1, 100)
    
    costo = round(random.uniform(5.0, 1000.0), 2)
    
    peso_base = random.randint(100, 800) 
    # Tolerancia entre 10g y 50g
    tolerancia = random.randint(10, 50) 
    
    peso_min = float(peso_base - tolerancia)
    peso_max = float(peso_base + tolerancia)
    
    pesos_panes = []
    estados = [] 
    conteo_defectuosos = 0
    
    for _ in range(num_panes):
        es_defectuoso = random.choice([True, False])
        
        if es_defectuoso:
            conteo_defectuosos += 1
            estados.append("D")
            if random.choice([True, False]):
                p = peso_min - random.uniform(1.0, 20.0)
            else:
                p = peso_max + random.uniform(1.0, 20.0)
        else:
            estados.append("C")
            p = random.uniform(peso_min + 0.1, peso_max - 0.1)
            
        pesos_panes.append(round(p, 2))

    total_perdido = conteo_defectuosos * costo

    array_string = ", ".join([f"{p:.2f}" for p in pesos_panes])
    
    c_test_code = f"float pesos[] = {{{array_string}}};\n"
    c_test_code += f"panesDefectuosos({num_panes}, {costo:.2f}, pesos, {peso_min:.2f}, {peso_max:.2f});"

    expected_output = f"{conteo_defectuosos}\n"
    expected_output += f"{total_perdido:.2f}\n"
    expected_output += " ".join(estados)

    return c_test_code, expected_output

if __name__ == "__main__":
    CANTIDAD_CASOS = 3
    
    print("="*40)
    print(f"GENERANDO {CANTIDAD_CASOS} CASOS DE PRUEBA")
    print("="*40)
    
    for i in range(1, CANTIDAD_CASOS + 1):
        codigo, salida = generar_testcase()
        
        print(f"\n--- TEST CASE {i} ---")
        print(">> TEST CODE (Copiar a CodeRunner):")
        print(codigo)
        print("\n>> EXPECTED OUTPUT (Copiar a CodeRunner):")
        print(salida)
        print("-" * 40)
