# 🧠 Generador de Dígitos Manuscritos para Material Educativo

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.2+-red.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38+-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Una aplicación de IA generativa que crea dígitos manuscritos ilimitados para material educativo**

[Características](#-características) • [Instalación](#-instalación) • [Uso](#-guía-de-uso) • [Arquitectura](#-arquitectura-técnica)

</div>

---

## 📋 Descripción del Proyecto

### Problemática

Los docentes de primaria necesitan constantemente ejemplos de dígitos manuscritos para:

- Ejercicios de matemáticas básicas
- Fichas de práctica de escritura
- Juegos educativos de reconocimiento numérico
- Material didáctico personalizado

Buscar o crear estas imágenes manualmente es tedioso y limita la variedad del material educativo.

### Solución

Esta aplicación web genera **imágenes de dígitos manuscritos (0-9) bajo demanda** utilizando una **DCGAN** (Deep Convolutional Generative Adversarial Network) entrenada sobre el dataset MNIST. Cada vez que se ejecuta, produce dígitos únicos con variaciones naturales de escritura manuscrita.

### ¿Qué la hace diferente?

✨ **Variedad infinita**: En lugar de reciclar un conjunto estático de imágenes, genera nuevos ejemplos cada vez.

🎯 **Específica para educación**: Diseñada pensando en las necesidades de docentes de primaria.

⚡ **Rápida y simple**: Interfaz intuitiva que no requiere conocimientos técnicos.

🎨 **Personalizable**: Elige cuántas imágenes generar en cada lote.

---

## ✨ Características

### Funcionales

- 🖼️ Generación de dígitos manuscritos (0-9) en alta calidad
- 🔢 Selección de cantidad de imágenes (4 a 64 por lote)
- 🔄 Generación ilimitada de nuevos ejemplos
- 👁️ Visualización en cuadrícula organizada
- 💾 Listo para captura o descarga

### Técnicas

- 🤖 Modelo DCGAN entrenado sobre MNIST
- 🔥 Backend en PyTorch
- 🌐 Interfaz web con Streamlit
- 📦 Gestión de dependencias con Poetry
- 🎲 Generación desde vectores de ruido latente (100 dimensiones)
- 🖥️ Soporte para CPU y GPU

---

## 🛠️ Arquitectura Técnica

### Stack Tecnológico

| Componente | Tecnología | Versión |
|------------|-----------|---------|
| Lenguaje | Python | 3.10+ |
| Framework ML | PyTorch | 2.2+ |
| UI | Streamlit | 1.38+ |
| Gestión de paquetes | Poetry | - |
| Dataset | MNIST | - |

### Arquitectura del Modelo

**Generador DCGAN**:

- **Entrada**: Vector de ruido latente (100 dimensiones)
- **Arquitectura**: 5 capas ConvTranspose2D con BatchNorm y ReLU
- **Salida**: Imagen 1x64x64 en escala de grises
- **Función de activación final**: Tanh (rango [-1, 1])

```bash
Input: Z (100, 1, 1)
  ↓ ConvTranspose2d + BatchNorm + ReLU
  → (512, 4, 4)
  ↓ ConvTranspose2d + BatchNorm + ReLU
  → (256, 8, 8)
  ↓ ConvTranspose2d + BatchNorm + ReLU
  → (128, 16, 16)
  ↓ ConvTranspose2d + BatchNorm + ReLU
  → (64, 32, 32)
  ↓ ConvTranspose2d + Tanh
Output: (1, 64, 64)
```

### Estructura del Proyecto

```bash
mnist-gan-app/
├── src/
│   ├── __init__.py
│   ├── app_streamlit.py      # Interfaz web principal
│   ├── config.py              # Configuración y rutas
│   ├── generator_service.py   # Lógica de generación
│   └── model.py               # Arquitectura del generador
├── model/
│   └── generator.pth          # Pesos del modelo entrenado
├── pyproject.toml             # Dependencias y configuración
├── .gitignore
└── README.md
```

---

## 📦 Instalación

### Requisitos Previos

- **Python 3.10 o superior** ([Descargar](https://www.python.org/downloads/))
- **Poetry** ([Guía de instalación](https://python-poetry.org/docs/#installation))
- **Archivo del modelo**: `generator.pth` (incluido en el repositorio)

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/lasanchezgi/mnist-gan-app.git
cd mnist-gan-app
```

2. **Verificar el modelo entrenado**

Asegúrate de que el archivo del modelo esté en su lugar:

```bash
ls model/generator.pth
```

Si no existe, copia el modelo entrenado desde tu notebook de entrenamiento:

```bash
cp /ruta/al/generator.pth model/generator.pth
```

3. **Instalar dependencias con Poetry**

```bash
poetry install
```

Esto creará automáticamente un entorno virtual e instalará:

- PyTorch 2.2+
- torchvision
- Streamlit
- NumPy
- Pillow

4. **Verificar la instalación**

```bash
poetry run python -c "import torch; import streamlit; print('✅ Instalación exitosa')"
```

---

## 🚀 Guía de Uso

### Iniciar la Aplicación

Desde el directorio raíz del proyecto:

```bash
poetry run streamlit run src/app_streamlit.py
```

La aplicación se abrirá automáticamente en tu navegador. Si no, accede manualmente a:

```bash
http://localhost:8501
```

### Interfaz de Usuario

#### Pantalla Principal

Al abrir la aplicación verás:

1. **Título y descripción**: Información sobre el propósito de la app
2. **Barra lateral (izquierda)**: Controles de generación
3. **Área central**: Zona de visualización de imágenes

#### Pasos para Generar Dígitos

1. **Ajustar cantidad de imágenes**
   - En la barra lateral, usa el control deslizante
   - Rango: 4 a 64 imágenes
   - Valor recomendado: 16 para balance entre variedad y rendimiento

2. **Generar dígitos**
   - Haz clic en el botón **"✨ Generar nuevos dígitos"**
   - Espera 1-2 segundos (dependiendo de tu hardware)
   - Los dígitos aparecerán en una cuadrícula

3. **Generar más ejemplos**
   - Vuelve a hacer clic en el botón para obtener dígitos completamente nuevos
   - Cada generación es única e impredecible

4. **Capturar o usar las imágenes**
   - Usa la herramienta de captura de tu sistema operativo
   - O haz clic derecho sobre la imagen y selecciona "Guardar imagen como..."

### Casos de Uso Educativo

#### 📝 Fichas de Práctica

Genera 16-25 dígitos variados para crear hojas de trabajo donde los estudiantes practiquen:

- Reconocimiento de números
- Copia de dígitos
- Ejercicios de conteo

#### 🎮 Juegos de Memoria

Genera pares de dígitos para:
- Juegos de memoria numérica
- Actividades de emparejamiento
- Tarjetas flash

#### 📊 Material de Evaluación

Crea conjuntos únicos de dígitos para:
- Exámenes de reconocimiento numérico
- Pruebas de lectura de números
- Evaluaciones sin riesgo de copia

---

## 🔧 Configuración Avanzada

### Parámetros del Modelo

Puedes modificar los parámetros en `src/config.py`:

```python
NZ = 100   # Dimensiones del vector de ruido latente
NGF = 64   # Feature maps del generador
NC = 1     # Canales de salida (1 = escala de grises)
```

⚠️ **Advertencia**: Solo modifica estos valores si reentrenaste el modelo con parámetros diferentes.

---

## 🧪 Solución de Problemas

### La aplicación no inicia

**Error**: `ImportError: attempted relative import with no known parent package`

**Solución**: Asegúrate de ejecutar desde la raíz del proyecto:

```bash
poetry run streamlit run src/app_streamlit.py
```

### No se encuentra el modelo

**Error**: `FileNotFoundError: No se encontró el archivo del modelo`

**Solución**: Verifica que `model/generator.pth` existe:

```bash
ls -lh model/generator.pth
```

### Generación muy lenta

**Problema**: La generación toma más de 5 segundos

**Soluciones**:

1. Reduce el número de imágenes en la barra lateral
2. Si tienes GPU NVIDIA, instala CUDA:

   ```bash
   poetry add torch torchvision --platform=cu118
   ```

3. Cierra otras aplicaciones pesadas

### Imágenes de baja calidad

**Problema**: Los dígitos no se ven bien formados

**Causa**: El modelo puede no estar bien entrenado

**Solución**: Asegúrate de usar el archivo `generator.pth` correcto entrenado por al menos 25 épocas

---

## 📚 Contexto Académico

Este proyecto fue desarrollado como parte de la **Evidencia de Aprendizaje 3** del curso de IA Generativa, demostrando:

- ✅ Implementación de un modelo generativo (DCGAN)
- ✅ Despliegue de una aplicación web funcional
- ✅ Solución a una problemática real (material educativo)
- ✅ Documentación técnica completa

---

## 🤝 Contribuciones

Este es un proyecto académico, pero sugerencias y mejoras son bienvenidas:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/MejoraDígitos`)
3. Commit tus cambios (`git commit -m 'Añadir mejora X'`)
4. Push a la rama (`git push origin feature/MejoraDígitos`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 👤 Autor

**Laura Sánchez Giraldo**

- Email: emailto:laurasanchezgiraldo@outlook.es

---

## 🙏 Agradecimientos

- Dataset MNIST por Yann LeCun et al.
- Comunidad de PyTorch por la documentación
- Streamlit por facilitar el desarrollo de interfaces web
- Docentes de primaria que inspiraron este proyecto

---

<div align="center">

**🌟 Si este proyecto te resulta útil, no olvides darle una estrella ⭐**

Hecho con ❤️ para educadores

</div>
