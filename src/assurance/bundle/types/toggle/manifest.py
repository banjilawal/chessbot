# src/assurance/manifest/types/toggle/manifest.py

"""
Module: assurance.manifest.types.toggle.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import ToggleBlueprint
from toggle import Toggle
from transit import ToggleCarrier


@dataclass(frozen=True)
class ToggleTypes(TypesManifest[Toggle]):
    model: Type[Toggle] = Toggle
    carrier: Type[ToggleCarrier] = ToggleCarrier
    blueprint: Type[ToggleBlueprint] = ToggleBlueprint