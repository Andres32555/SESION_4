"""
Sesion 4 - Taller de Laboratorio: Motor Logico de Recursos Humanos (40 MIN)
Bono anual en funcion del Desempeno y la Antiguedad del empleado.
"""

# Paso 1: variables difusas (grados de membresia ya fuzzificados)
grados = {
    "desempeno_pobre": 0.1,
    "desempeno_promedio": 0.3,
    "desempeno_excelente": 0.85,
    "antiguedad_corta": 0.2,
    "antiguedad_larga": 0.6,
}


# Paso 2 y 3: motor con 3 reglas logicas (min = AND, max = OR)
def evaluar_reglas_bono(grados):
    # R1: SI Desempeno es Pobre O Antiguedad es Corta -> Bono Bajo
    activacion_bajo = max(grados["desempeno_pobre"], grados["antiguedad_corta"])

    # R2: SI Desempeno es Promedio -> Bono Medio
    activacion_medio = grados["desempeno_promedio"]

    # R3: SI Desempeno es Excelente Y Antiguedad es Larga -> Bono Alto
    activacion_alto = min(grados["desempeno_excelente"], grados["antiguedad_larga"])

    return {"BAJO": activacion_bajo, "MEDIO": activacion_medio, "ALTO": activacion_alto}


if __name__ == "__main__":
    niveles_bono = evaluar_reglas_bono(grados)
    print("Fuerza de activación por nivel de bono:", niveles_bono)

    # Paso 4: Pregunta teorica - Agregacion Mamdani con T-Conorma (OR = max)
    fuerza_regla_a = 0.4  # otra regla que tambien concluye "Bono Alto"
    fuerza_regla_b = 0.7
    fuerza_final_bono_alto = max(fuerza_regla_a, fuerza_regla_b)
    print("Fuerza final agregada para 'Bono Alto':", fuerza_final_bono_alto)
