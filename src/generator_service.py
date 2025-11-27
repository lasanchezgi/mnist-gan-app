# src/generator_service.py

from typing import Tuple

import numpy as np
import torch
from torchvision.utils import make_grid

from src.config import MODEL_PATH, NC, NGF, NZ
from src.model import Generator


class DigitGeneratorService:
    """
    Servicio encargado de:
    - Cargar el modelo entrenado.
    - Generar imágenes a partir de ruido.
    """

    def __init__(self, device: str | None = None) -> None:
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(device)

        self._generator = self._load_generator()

    def _load_generator(self) -> Generator:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo del modelo en {MODEL_PATH}. "
                f"Asegúrate de haber copiado 'generator.pth' desde tu notebook."
            )

        generator = Generator(nz=NZ, ngf=NGF, nc=NC).to(self.device)
        state_dict = torch.load(MODEL_PATH, map_location=self.device)
        generator.load_state_dict(state_dict)
        generator.eval()
        return generator

    @torch.no_grad()
    def generate_grid(self, num_images: int = 16) -> np.ndarray:
        """
        Genera 'num_images' dígitos y devuelve una cuadrícula como imagen (numpy array)
        lista para mostrar en Streamlit.
        """
        # sqrt para armar cuadrícula cuadrada
        nrow = int(np.ceil(np.sqrt(num_images)))

        noise = torch.randn(num_images, NZ, 1, 1, device=self.device)
        fake_images = self._generator(noise).cpu()

        # make_grid combina las imágenes en una sola
        grid = make_grid(fake_images, nrow=nrow, normalize=True, pad_value=1.0)

        # De Tensor [C, H, W] → Numpy [H, W, C]
        grid_np = grid.numpy()
        grid_np = np.transpose(grid_np, (1, 2, 0))

        return grid_np
