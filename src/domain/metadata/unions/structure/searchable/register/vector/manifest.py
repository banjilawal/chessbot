# src/domain/metadata/unions/structureregister/vector/manifest.py

"""
Module: domain.metadata.unions.structure.searchable.register.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import RegisterUnions
from fabrication import VectorRegisterBlueprint
from domain.structure.register import VectorRegister
from transit.carrier import VectorRegisterCarrier


@dataclass
class VectorRegisterUnions(RegisterUnions):
    model: Type[VectorRegister] = VectorRegister
    carrier: Type[VectorRegisterCarrier] = VectorRegisterCarrier
    blueprint: Type[VectorRegisterBlueprint] = VectorRegisterBlueprint