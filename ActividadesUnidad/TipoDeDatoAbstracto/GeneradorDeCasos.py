import random
import string

def random_str(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def random_email():
    return f"{random_str(5)}@{random_str(4)}.com"

num_users = random.randint(3, 25) # Entre 3 y 6 usuarios
users_data = []

print("Perfil usuarios[] = {")
for i in range(num_users):
    u_name = f"user_{random_str(8)}"
    u_email = random_email()
    u_pass = random_str(12)
    u_posts = random.randint(0, 20)
    
    users_data.append({'name': u_name, 'pass': u_pass})
    
    # Imprimir línea de C
    coma = "," if i < num_users - 1 else ""
    print(f'    {{"{u_name}", "{u_email}", "{u_pass}", {u_posts}}}{coma}')
print("};")

print("")

num_queries = random.randint(5, 40)
queries_c_lines = []

# Forzamos que la primera consulta sea siempre un SELECT para evitar modificar "nada"
current_user_idx = random.randint(0, num_users - 1)
queries_c_lines.append(f'{{"SELECT", "NA", "{current_user_idx}"}}')

for _ in range(num_queries - 1):
    tipo = random.choices(["SELECT", "MODIFY"], weights=[30, 70], k=1)[0]
    
    if tipo == "SELECT":
        current_user_idx = random.randint(0, num_users - 1)
        queries_c_lines.append(f'{{"SELECT", "NA", "{current_user_idx}"}}')
    else:
        # MODIFY
        campo = random.choice(["username", "email", "password", "new_post"])
        valor = "NA"
        
        if campo == "username":
            valor = f"mod_{random_str(4)}"
        elif campo == "email":
            valor = random_email()
        elif campo == "password":
            # 20% de probabilidad de usar la MISMA contraseña actual para probar el error
            if random.random() < 0.2:
                valor = users_data[current_user_idx]['pass']
            else:
                valor = random_str(8)
                # Actualizamos nuestra "memoria" de la contraseña (simplificado)
                users_data[current_user_idx]['pass'] = valor 
                
        queries_c_lines.append(f'{{"MODIFY", "{campo}", "{valor}"}}')

print("Consulta consultas[] = {")
for i, line in enumerate(queries_c_lines):
    coma = "," if i < len(queries_c_lines) - 1 else ""
    print(f'    {line}{coma}')
print("};")

print("") # Espacio

print(f"int n = {num_users};")
print(f"int m = {len(queries_c_lines)};")
print("")
print("procesarConsultas(n, usuarios, m, consultas);")
