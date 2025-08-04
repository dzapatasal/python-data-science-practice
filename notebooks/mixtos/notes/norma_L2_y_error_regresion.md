# Términos Matemáticos Clave en Modelos de Regresión

Este documento explica conceptos matemáticos fundamentales utilizados en modelos de regresión, especialmente la relación entre la norma euclidiana (L2) y la evaluación del error en modelos predictivos.

## 📏 Relación entre la norma euclidiana (L2) y un modelo de regresión

Un modelo de regresión (como la regresión lineal) intenta encontrar la **"mejor" línea** (o curva) que se ajuste a tus datos.  
La **norma euclidiana** es como su **"brújula"** para medir el error y decidir cuál es la mejor línea.

---

### 🔧 ¿Cómo la usa el modelo?

1. **Calcula errores:**  
   Para cada dato, mide la **distancia vertical (error)** entre el valor real (`y`) y lo que predice el modelo (`ŷ`).

2. **Suma los errores al cuadrado:**  
   Usa la **norma L2** para convertir esos errores en un solo número:  
   la **"distancia total"** del error (también llamada *error cuadrático total*).

3. **Ajusta la línea:**  
   El modelo **mueve la línea** (es decir, cambia los coeficientes como `a` y `b`)  
   para **minimizar ese error total** y así encontrar el mejor ajuste posible.

🧠 En resumen:  
La **norma L2** ayuda al modelo a saber **cuán lejos están sus predicciones de la realidad** y a **mejorar la precisión** de la línea de regresión.

---

## 🧮 Interpretación del Error en un Modelo de Precios

**Ejemplo basado en el archivo [`np_pd_apples.ipynb`](../mixtos/np_pd_apples.ipynb):**

### 1. Interpretación del Error (103.53 soles)

- **No es el error por observación individual**, sino la **suma acumulada** de errores en distancia euclidiana (L2) para las 87 observaciones.
- **Cálculo del error promedio:**  
  $$
  \text{Error promedio} = \frac{103.53}{87} \approx 1.19 \text{ soles por observación}
  $$
- **Significado:**  
  Las predicciones (`y`) se desvían en promedio **1.19 soles** de los valores reales (`Moscu`).

---

### 2. ¿Es un error aceptable?

**Depende del contexto:**

#### 🔹 Para modelos de predicción en tiempo real
- ✅ **Excelente precisión** (error de ~1.19 soles con precios entre 73-131 soles).
- 📌 Ejemplo práctico:  
  - Precio real: 100.00 soles  
  - Predicción típica: entre 98.81 y 101.19 soles  
  - Margen mínimo para aplicaciones comerciales.

---

### 📊 Resumen de Interpretación

| Contexto                  | Evaluación                   | Acción Recomendada              |
|---------------------------|------------------------------|---------------------------------|
| Predicción en tiempo real | Error mínimo (1.19 soles)    | Validar con nuevos datos        |
| Análisis económico        | Requiere métricas adicionales| Calcular MAPE y RMSE            |

---

## Referencias

- Aplicación práctica: [np_pd_apples.ipynb](../mixtos/np_pd_apples.ipynb)