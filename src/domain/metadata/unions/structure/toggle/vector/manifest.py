# src/domain/metadata/unions/structuretoggle/vector/manifest.py

"""
Module: domain.metadata.unions.structure.toggle.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import ToggleUnions
from fabrication import VectorToggleBlueprint
from domain.structure.toggle import CartesianToggle
from transit.carrier import VectorToggleCarrier


@dataclass
class VectorToggleUnions(ToggleUnions):
    model: Type[CartesianToggle] = CartesianToggle
    carrier: Type[VectorToggleCarrier] = VectorToggleCarrier
    blueprint: Type[VectorToggleBlueprint] = VectorToggleBlueprint