# src/model.py

from typing import Any
import torch.nn as nn


class Generator(nn.Module):
    """
    Generador de la DCGAN para dígitos MNIST (1 x 64 x 64).
    Debe coincidir exactamente con la arquitectura usada en el entrenamiento.
    """

    def __init__(self, nz: int, ngf: int, nc: int) -> None:
        super().__init__()
        self.main = nn.Sequential(
            # Entrada: Z → (nz, 1, 1)
            nn.ConvTranspose2d(nz, ngf * 8, kernel_size=4, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(ngf * 8),
            nn.ReLU(True),  # (ngf*8) x 4 x 4

            nn.ConvTranspose2d(ngf * 8, ngf * 4, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf * 4),
            nn.ReLU(True),  # (ngf*4) x 8 x 8

            nn.ConvTranspose2d(ngf * 4, ngf * 2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True),  # (ngf*2) x 16 x 16

            nn.ConvTranspose2d(ngf * 2, ngf, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),  # (ngf) x 32 x 32

            nn.ConvTranspose2d(ngf, nc, kernel_size=4, stride=2, padding=1, bias=False),
            nn.Tanh(),  # (nc) x 64 x 64 en [-1, 1]
        )

    def forward(self, x: Any) -> Any:
        return self.main(x)
