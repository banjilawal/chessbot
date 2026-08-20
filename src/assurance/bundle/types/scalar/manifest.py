# src/assurance/manifest/types/scalar/manifest.py

"""
Module: assurance.manifest.types.scalar.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import ScalarBlueprint
from model import Scalar
from transit import ScalarCarrier


@dataclass(frozen=True)
class ScalarTypes(TypesManifest[Scalar]):
    model: Type[Scalar] = Scalar
    carrier: Type[ScalarCarrier] = ScalarCarrier
    blueprint: Type[ScalarBlueprint] = ScalarBlueprint