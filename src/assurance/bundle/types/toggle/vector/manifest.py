# src/assurance/manifest/types/toggle/vector/manifest.py

"""
Module: assurance.manifest.types.toggle.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import ToggleTypes
from fabrication import VectorToggleBlueprint
from domain.toggle import CartesianToggle
from transit import VectorToggleCarrier


@dataclass
class VectorToggleTypes(ToggleTypes):
    model: Type[CartesianToggle] = CartesianToggle
    carrier: Type[VectorToggleCarrier] = VectorToggleCarrier
    blueprint: Type[VectorToggleBlueprint] = VectorToggleBlueprint