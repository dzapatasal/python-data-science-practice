# Tareas asignadas
```
Curso Pandas: conociendo la biblioteca
```
## Parte 1: (Completado) ✅
- Importa el archivo 'alumnos.csv' y almacena su contenido en un DataFrame de Pandas.
- Visualiza las primeras 7 filas del DataFrame y las últimas 5.
- Verifica la cantidad de filas y columnas en este DataFrame.
- Explora las columnas del DataFrame y analiza los tipos de datos presentes en cada columna.

**Extra**: Calcula algunas estadísticas descriptivas básicas de los datos en el DataFrame (media, desviación estándar, etc.). Pista: busca el método "describe".

## Parte 2: (Completado) ✅

- Verifica si la base de datos contiene datos nulos y, en caso de tenerlos, realiza el tratamiento de estos datos nulos de la manera que consideres más coherente con la situación.
- Los estudiantes "Alicia" y "Carlos" ya no forman parte del grupo. Por lo tanto, elimínalos de la base de datos.
- Aplica un filtro que seleccione solo a los estudiantes que fueron aprobados.
- Guarda el DataFrame que contiene solo a los estudiantes aprobados en un archivo CSV llamado "alumnos_aprobados.csv".

**Extra**: Al revisar las calificaciones de los estudiantes aprobados, notamos que algunas calificaciones eran incorrectas. Las estudiantes que obtuvieron una calificación de 7.0, en realidad tenían un punto extra que no se contabilizó. Por lo tanto, reemplaza las calificaciones de 7.0 en la base de datos por 8.0. Consejo: busca el método replace.

## Parte 3: (Pendiente) ☐

- Los estudiantes participaron en una actividad extracurricular y ganaron puntos extras. Estos puntos extras corresponden al 40% de su nota actual. Por lo tanto, crea una columna llamada "Puntos_extras" que contenga los puntos extras de cada estudiante, es decir, el 40% de su nota actual.

- Crea otra columna llamada "Notas_finales" que contenga las notas de cada estudiante sumadas con los puntos extras.

- Dado que hubo una puntuación extra, algunos estudiantes que no habían sido aprobados antes pueden haber sido aprobados ahora. En función de esto, crea una columna llamada "Aprobado_final" con los siguientes valores:

    - True: si el estudiante está aprobado (la nota final debe ser mayor o igual a 7.0).
    - False: si el estudiante está reprobado (la nota final debe ser menor que 7.0).

Realiza una selección y verifica qué estudiantes no habían sido aprobados anteriormente, pero ahora fueron aprobados después de sumar los puntos extras.