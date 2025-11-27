# 🧠 Generador de dígitos manuscritos (DCGAN + MNIST)

Este proyecto es un **ejemplo sencillo** de aplicación de IA generativa para la Evidencia de Aprendizaje 3.

La app carga un modelo **DCGAN** entrenado sobre **MNIST** y permite generar imágenes de dígitos manuscritos desde una interfaz web en **Streamlit**.

---

## ✅ Requisitos previos

- Python 3.10 o superior
- [Poetry](https://python-poetry.org/docs/#installation) instalado
- Archivo `generator.pth` exportado desde el notebook de entrenamiento

---

## 📦 Instalación del proyecto

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/mnist-gan-app.git
cd mnist-gan-app
```

2. **Copiar el modelo entrenado**

Copia el archivo generator.pth generado en el notebook a la carpeta models/:

```bash
cp /ruta/al/generator.pth models/generator.pth`
```

3. **Instalar dependencias con Poetry**

```bash
poetry install
```

Esto creará un entorno virtual e instalará todas las librerías necesarias
(`torch`, `torchvision`, `streamlit`, etc.).

## ▶️ Ejecutar la aplicación

Dentro del directorio del proyecto:

```bash
poetry run streamlit run src/app_streamlit.py
```

Luego abre en el navegador la URL que te muestra Streamlit, normalmente:

```bash
http://localhost:8501
```

## 👩‍🏫 Guía rápida de uso

1. Abre la app en el navegador.
2. En la barra lateral, elige cuántas imágenes quieres generar.
3. Haz clic en "✨ Generar nuevos dígitos".
4. Observa la cuadrícula de dígitos generados.
5. Vuelve a presionar el botón para generar un nuevo conjunto.
