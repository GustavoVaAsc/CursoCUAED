import subprocess, json, sys, time

is_precheck = {{ IS_PRECHECK }}
student_code = """{{ STUDENT_ANSWER | e('py') }}"""

# Definimos las librerías y las estructuras requeridas ANTES del código 
# del estudiante, para que su función las pueda reconocer.
c_source = r"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    char nombreUsuario[21]; 
    char correo[65];        
    char contrasena[33];    
    int publicaciones;
} Perfil;

typedef struct {
    char tipo[10];
    char campo[20];
    char valor[65];
} Consulta;

""" + student_code + r"""

int main() {
    int testNum = 0;
    if(scanf("%d", &testNum) != 1) return 1;

""" + """
{% for TEST in TESTCASES %}
    if (testNum == {{ loop.index0 }}) {
        {{ TEST.testcode }};
    }
{% endfor %}
""" + r"""
    return 0;
}
"""

with open('solution.c', 'w') as f:
    f.write(c_source)

compile_result = subprocess.run(
    ['gcc', '-o', 'solution', 'solution.c', '-Wall'],
    capture_output=True, universal_newlines=True
)

if compile_result.returncode != 0:
    error_msg = compile_result.stderr.strip()
    result = {
        "fraction": 0.0,
        "prologuehtml": f"""
            <div style='color:red; font-family:monospace; background:#fff0f0;
                        padding:10px; border-left: 4px solid red;'>
                <strong>❌ Error de compilación:</strong><br>
                <pre>{error_msg}</pre>
            </div>
        """,
        "testresults": [["iscorrect", "Test", "Esperado", "Obtenido", "Veredicto"]]
    }
    print(json.dumps(result))
    sys.exit(0)

def run_with_timeout(test_index, time_limit):
    """
    Usa el comando nativo 'timeout' de Linux. 
    Si excede el tiempo, devuelve código de salida 124.
    """
    try:
        proc = subprocess.run(
            ['timeout', str(time_limit), './solution'],
            input=str(test_index),
            capture_output=True,
            text=True
        )
        
        timed_out = (proc.returncode == 124)
        return proc.stdout.strip(), proc.stderr.strip(), proc.returncode, timed_out
    except Exception as e:
        return "", str(e), -1, False

testcases = [
{% for TEST in TESTCASES %}
    {
        "testcode": """{{ TEST.testcode | e('py') }}""",
        "expected": """{{ TEST.expected | e('py') }}""",
        "index":    {{ loop.index0 }},
        "display":  "{{ TEST.display }}",
    },
{% endfor %}
]

rows = []
passed = 0
tle_count = 0
error_count = 0
wrong_count = 0

GLOBAL_TIME_BUDGET = 2.0  
MAX_TIME_PER_TEST = 0.4
start_time = time.time()

for tc in testcases:
    elapsed_time = time.time() - start_time
    time_left = GLOBAL_TIME_BUDGET - elapsed_time

    if time_left <= 0.1:
        got, stderr, returncode, timed_out = "", "", -1, True
    else:
        current_limit = min(MAX_TIME_PER_TEST, time_left)
        got, stderr, returncode, timed_out = run_with_timeout(tc['index'], current_limit)

    if timed_out:
        got = "(sin salida)"
        verdict = "⏱️ Tiempo excedido. ¿Podrías mejorar su tiempo de ejecución?"
        correct = 0
        tle_count += 1
    elif returncode != 0 or stderr:
        # Pista explícita de Seg Fault adaptada para arreglos y strings
        got = stderr if stderr else "(Fallo de segmentación / core dumped)"
        verdict = "💥 Segmentation Fault (Revisa tu uso de strcpy, strcmp o los índices de tus arreglos)"
        correct = 0
        error_count += 1
    elif got == tc['expected'].strip():
        verdict = "✅ Correcto"
        correct = 1
        passed += 1
    else:
        verdict = "❌ Incorrecto"
        correct = 0
        wrong_count += 1

    rows.append([correct, tc['testcode'], tc['expected'].strip(), got, verdict])

total = len(testcases)
fraction = passed / total if total > 0 else 0.0

def build_prologue(passed, total, tle_count, error_count, wrong_count, is_precheck):
    if passed == total:
        if is_precheck:
            return "<div style='color:green;'>✅ <strong>¡Prechecks correctos!</strong> Envía tu código para la calificación final.</div>"
        return "<div style='color:green;'>🎉 ¡Correcto! La migración de DelayedMeter se realizó con éxito.</div>"

    issues = []
    if tle_count > 0: issues.append(f"⏱️ <strong>{tle_count}</strong> caso(s) con tiempo límite excedido")
    if error_count > 0: issues.append(f"💥 <strong>{error_count}</strong> caso(s) con <strong>Segmentation Fault</strong> (Generalmente ocurre al copiar cadenas más grandes que el destino o acceder a índices fuera de rango)")
    if wrong_count > 0: issues.append(f"❌ <strong>{wrong_count}</strong> caso(s) con respuesta incorrecta (Verifica la lógica del MODIFY y el formato de impresión)")
    
    issues_html = "<ul>" + "".join(f"<li>{i}</li>" for i in issues) + "</ul>"

    if is_precheck:
        return f"<div style='color:red;'>⚠️ <strong>Precheck fallido</strong> ({passed}/{total}).<br>{issues_html}</div>"

    color = "red" if fraction < 0.5 else "orange"
    return f"<div style='color:{color};'>⚠️ Pasaste <strong>{passed} de {total}</strong> pruebas.<br>{issues_html}</div>"

print(json.dumps({
    "fraction": fraction,
    "prologuehtml": build_prologue(passed, total, tle_count, error_count, wrong_count, is_precheck),
    "testresults": [["iscorrect", "Test", "Esperado", "Obtenido", "Veredicto"]] + rows
}))
