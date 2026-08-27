# src/domain/metadata/unions/structureregister/manifest.py

"""
Module: domain.metadata.unions.structure.searchable.register.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import UnionsManifest
from fabrication import RegisterBlueprint
from domain.structure.register import Register
from transit.carrier import RegisterCarrier


@dataclass
class RegisterUnions(UnionsManifest[Register]):
    model: Type[Register] = Register
    carrier: Type[RegisterCarrier] = RegisterCarrier
    blueprint: Type[RegisterBlueprint] = RegisterBlueprint