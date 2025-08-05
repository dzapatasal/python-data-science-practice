# Manual de Proyecto: Análisis de Inmuebles CDMX

## Descripción general
Este proyecto consiste en el análisis de una base de datos de inmuebles en la Ciudad de México, con el objetivo de brindar soporte tanto al equipo de Aprendizaje Automático (ML) como al equipo de Desarrollo (DEV) de una empresa inmobiliaria.

## Etapas y tareas principales (según Trello)

### 1. Importar y conocer la base de datos
- Importar los datos desde el archivo 'alquiler.csv'.
- Verificar cantidad de filas y columnas.
- Explorar las columnas y sus tipos de datos.

### 2. Tratar valores nulos
- Verificar la existencia de datos nulos.
- Tratar los datos nulos para que sean aptos para ML.

### 3. Remover registros inconsistentes
- Eliminar departamentos con valor de alquiler igual a 0.
- Eliminar departamentos con condominio igual a 0.

### 4. Análisis exploratorio de los datos (EDA)
- Calcular valores promedio de alquiler por tipo de inmueble residencial.
- Calcular el porcentaje de cada tipo de inmueble presente en la base de datos.
- Formular y responder preguntas clave sobre los datos.

### 5. Aplicar filtros específicos para ML
- Filtrar apartamentos con 1 dormitorio y alquiler menor a MXN 4200.
- Filtrar apartamentos con al menos 2 dormitorios, alquiler menor a MXN 10500 y superficie mayor a 70 m².

### 6. Crear columnas adicionales para DEV
- Crear columna **valor_mensual**:
    - gastos mensuales de cada propiedad + alquiler + condominio 
- Crear columna **valor_anual**: 
    - gasto anual por propiedad (impuesto + 12 meses de alquiler y condominio).
- Crear columna **Suites**: 
    - indique únicamente si la propiedad tiene o no suites, sin importar la cantidad.

### 7. Guardar los datos finales
- Almacenar los DataFrames procesados en formato CSV.

## Referencia al tablero Trello
- [Tablero Trello: Pandas, conociendo la Biblioteca](https://trello.com/b/Klvp5qky/pandas-conociendo-la-biblioteca)

## Notas
- Cada etapa puede contener subtareas y checklist para asegurar la calidad del análisis.
- El flujo de trabajo sigue el orden: Backlog → En desarrollo → Concluído.
- Documenta cualquier decisión importante o hallazgo relevante durante el análisis.