# src/assurance/manifest/types/square/manifest.py

"""
Module: assurance.manifest.types.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import SquareBlueprint
from model import Square
from transit import SquareCarrier


@dataclass(frozen=True)
class SquareTypes(TypesManifest[Square]):
    model: Type[Square] = Square
    carrier: Type[SquareCarrier] = SquareCarrier
    blueprint: Type[SquareBlueprint] = SquareBlueprint