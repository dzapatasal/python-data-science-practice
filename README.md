
# Práctica de Análisis de Datos con Python y Pandas

<p align="center">
  <img src="https://img.shields.io/badge/Proyecto-Análisis_de_Datos-blueviolet?style=flat-square" alt="Proyecto">
  <img src="https://img.shields.io/badge/Estado-En%20Desarrollo-yellow?style=flat-square" alt="Estado">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat-square&logo=jupyter" alt="Jupyter Notebook">
  <img src="https://img.shields.io/badge/Dependencias-Numpy%20%7C%20Pandas%20%7C%20Matplotlib-informational?style=flat-square" alt="Dependencias">
</p>

## 📝 Descripción del Proyecto

Este repositorio contiene un proyecto de práctica enfocado en el análisis y manipulación de datos utilizando las librerías `Numpy` y `Pandas` en Python. El objetivo es aplicar las herramientas de la ciencia de datos a un conjunto de datos simple para explorar y obtener información relevante, sirviendo como un entorno de aprendizaje para el manejo de datos tabulares.

## 📁 Estructura del Repositorio

La estructura del repositorio está organizada de la siguiente manera:

```
├── .gitignore
├── datasets/
│   └── apples\_ts.csv
├── notebooks/
│   └── mixtos/
│       └── np\_pd\_apples.ipynb
├── utils/
│   └── helpers.py
└── ven/
```

- `notebooks/mixtos/`: Contiene el cuaderno de Jupyter (`np_pd_apples.ipynb`) donde se realiza el análisis.
- `datasets/`: Almacena el archivo CSV con los datos a analizar (`apples_ts.csv`).
- `utils/`: Módulo de Python (`helpers.py`) que podría contener funciones auxiliares para el análisis.
- `ven/`: La carpeta del entorno virtual, ignorada por Git.

## 🚀 Análisis Realizado

En el cuaderno `np_pd_apples.ipynb` se llevan a cabo los siguientes pasos:

1.  **Carga de Datos**: Se utiliza `pandas` para cargar el archivo `apples_ts.csv` en un DataFrame.
2.  **Exploración Inicial**: Se realiza una exploración de los datos para entender su estructura, tipos de datos y valores faltantes.
3.  **Manipulación de Datos**: Se aplican funciones de `numpy` y `pandas` para limpiar, filtrar o transformar los datos.
4.  **Análisis Descriptivo**: Se calculan estadísticas descriptivas básicas para resumir las características principales de los datos.
5.  **Visualización (Opcional)**: Se pueden incluir gráficos simples para visualizar tendencias o patrones en los datos.

## 🔧 Instalación y Uso

Sigue estos pasos para configurar el proyecto en tu máquina y ejecutar el cuaderno.

### Requisitos
-   Python 3.8+
-   Jupyter Notebook

### Dependencias
Para instalar las librerías necesarias, activa tu entorno virtual y ejecuta el siguiente comando:

```bash
pip install numpy pandas jupyter
```

### Pasos para la ejecución

1.  Clonar el repositorio:
    ```bash
    git clone [https://m.youtube.com/watch?v=KrJwqsuhZ8U&pp=0gcJCYUJAYcqIYzv](https://m.youtube.com/watch?v=KrJwqsuhZ8U&pp=0gcJCYUJAYcqIYzv)
    cd [nombre de tu proyecto]
    ```
2.  Activar tu entorno virtual (`ven`):
      - En Windows: `.\ven\Scripts\activate`
      - En macOS/Linux: `source ven/bin/activate`
3.  Abrir el cuaderno:
    Abre VS Code y navega hasta `notebooks/mixtos/np_pd_apples.ipynb` para ejecutar el código.

## 📜 Licencia

Este proyecto es de uso libre y educativo, sin licencia específica.

## 🙏 Agradecimientos

Proyecto desarrollado como parte de un proceso de aprendizaje autodidacta.
