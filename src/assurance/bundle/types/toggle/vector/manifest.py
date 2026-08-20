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
from toggle import VectorToggle
from transit import VectorToggleCarrier


@dataclass(frozen=True)
class VectorToggleTypes(ToggleTypes):
    model: Type[VectorToggle] = VectorToggle
    carrier: Type[VectorToggleCarrier] = VectorToggleCarrier
    blueprint: Type[VectorToggleBlueprint] = VectorToggleBlueprint