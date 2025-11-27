# src/config.py

from pathlib import Path

# Ruta base del proyecto (asumiendo que se ejecuta desde el directorio raíz)
BASE_DIR = Path(__file__).resolve().parents[1]

# Ruta del modelo guardado
MODEL_PATH = BASE_DIR / "model" / "generator.pth"

# Parámetros del modelo (deben coincidir con el notebook)
NZ = 100  # tamaño del vector de ruido
NGF = 64  # feature maps en el generador
NC = 1    # canales de la imagen (1 = escala de grises)
