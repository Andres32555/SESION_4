# Sesión 4 — Inferencia Difusa (Modelo Mamdani)

Taller Analítico: Propagación de Fuerza (20 min)

Regla: `R1: SI (Rentabilidad es ALTA) O (Impacto_Social es ALTO) Y (Riesgo es BAJO) ENTONCES (Aprobación es SEGURA)`

Grados de membresía del Proyecto X:
`Rentabilidad ALTA = 0.6`, `Impacto_Social ALTO = 0.2`, `Riesgo BAJO = 0.4`

Paso 1 — Calcular la fuerza de la premisa completa (precedencia: el OR entre paréntesis primero)

1. Evaluar el paréntesis OR (T-Conorma = `max`):
   `max(Rentabilidad_ALTA, Impacto_Social_ALTO) = max(0.6, 0.2) = 0.6`
2. Evaluar el AND con Riesgo BAJO (T-Norma = `min`):
   `min(0.6, Riesgo_BAJO) = min(0.6, 0.4) = 0.4`

Fuerza de activación de la regla = 0.4

Paso 2 — Altura de truncamiento de la conclusión

El conjunto difuso "Aprobación SEGURA" se **trunca a una altura máxima Y = 0.4**, tal como se implementa después con `min(fuerza_or, grados["riesgo_bajo"])` en el código de la sesión.


Taller de Laboratorio: Motor Lógico de Recursos Humanos (40 min)

Misión práctica:

1. Diccionario con variables difusas de *Desempeño* y *Antigüedad* (ej. `desempeno_pobre = 0.1`, `desempeno_excelente = 0.85`, `antiguedad_larga = 0.6`, etc.).
2. Programar 3 reglas lógicas con `min()`/`max()`:
   - R1: SI Desempeño es Pobre O Antigüedad es Corta → Bono Bajo.
   - R2: SI Desempeño es Promedio → Bono Medio.
   - R3: SI Desempeño es Excelente Y Antigüedad es Larga → Bono Alto.
3. El motor retorna un diccionario con los niveles de activación de Bono Bajo, Medio y Alto.
4. Pregunta teórica: si dos reglas distintas concluyen en "Bono Alto" (con fuerzas 0.4 y 0.7), el paso de **Agregación** de Mamdani exige unificar con la **T-Conorma (OR = `max`)**.
   → `fuerza_final_bono_alto = max(0.4, 0.7) = 0.7`. Se usa `max` (no una suma) porque el grado de verdad agregado nunca puede superar 1.0; basta con que la regla más fuerte determine la altura final del conjunto difuso resultante antes de la defuzzificación.

