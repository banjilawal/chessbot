# src/domain/metadata/unions/structuretoggle/manifest.py

"""
Module: domain.metadata.unions.structure.toggle.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import UnionsManifest
from fabrication import ToggleBlueprint
from domain.structure.toggle import Toggle
from domain.transit import ToggleCarrier


@dataclass
class ToggleUnions(UnionsManifest[Toggle]):
    model: Type[Toggle] = Toggle
    carrier: Type[ToggleCarrier] = ToggleCarrier
    blueprint: Type[ToggleBlueprint] = ToggleBlueprint