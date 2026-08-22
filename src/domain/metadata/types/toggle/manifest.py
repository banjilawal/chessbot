# src/domain/metadata/types/toggle/manifest.py

"""
Module: domain.metadata.types.toggle.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import ToggleBlueprint
from domain.structure.toggle import Toggle
from domain.transit import ToggleCarrier


@dataclass
class ToggleTypes(TypesManifest[Toggle]):
    model: Type[Toggle] = Toggle
    carrier: Type[ToggleCarrier] = ToggleCarrier
    blueprint: Type[ToggleBlueprint] = ToggleBlueprint