import random
import string

def random_pid():
    return random.randint(100, 999)

def random_name():
    apps = ["Chrome", "Firefox", "Word", "Excel", "Code", "Discord", "Spotify", "Slack", "Zoom", "Docker", "Python", "System"]
    return random.choice(apps) + "_" + ''.join(random.choices(string.digits, k=2))
  
num_ops = random.randint(8, 15) # Cantidad total de operaciones
ops_c_lines = []

# Solo guardamos los PIDs para saber a quién matar
active_pids = []

cap_inicial = random.randint(2, 4) # Pequeña para forzar reallocs
ops_c_lines.append(f'{{"INIT", {cap_inicial}, ""}}')

for _ in range(num_ops):
    # Pesos: 50% ADD, 30% STATUS, 20% KILL
    accion = random.choices(["ADD", "STATUS", "KILL"], weights=[50, 30, 20], k=1)[0]
    
    if accion == "ADD":
        pid = random_pid()
        # Asegurar PIDs únicos en nuestra simulación simple
        while pid in active_pids:
            pid = random_pid()
            
        name = random_name()
        active_pids.append(pid)
        ops_c_lines.append(f'{{"ADD", {pid}, "{name}"}}')
        
    elif accion == "KILL":
        if active_pids and random.random() > 0.3:
            # 70% probabilidad de matar un PID existente
            target_pid = random.choice(active_pids)
            active_pids.remove(target_pid)
        else:
            # 30% probabilidad de intentar matar un PID inexistente
            target_pid = random.randint(1000, 9999)
            
        ops_c_lines.append(f'{{"KILL", {target_pid}, ""}}')
        
    elif accion == "STATUS":
        ops_c_lines.append(f'{{"STATUS", 0, ""}}')

ops_c_lines.append(f'{{"STATUS", 0, ""}}')

print("Operacion ops[] = {")
for i, line in enumerate(ops_c_lines):
    coma = "," if i < len(ops_c_lines) - 1 else ""
    print(f'    {line}{coma}')
print("};")

print("")
print(f"int n = {len(ops_c_lines)};")
print("gestionarProcesos(n, ops);")
