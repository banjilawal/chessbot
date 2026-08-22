# src/domain/metadata/types/register/vector/manifest.py

"""
Module: domain.metadata.types.register.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import RegisterTypes
from fabrication import VectorRegisterBlueprint
from domain.structures.register import VectorRegister
from domain.transit import VectorRegisterCarrier


@dataclass
class VectorRegisterTypes(RegisterTypes):
    model: Type[VectorRegister] = VectorRegister
    carrier: Type[VectorRegisterCarrier] = VectorRegisterCarrier
    blueprint: Type[VectorRegisterBlueprint] = VectorRegisterBlueprint