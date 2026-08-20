# src/assurance/manifest/types/register/vector/manifest.py

"""
Module: assurance.manifest.types.register.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import RegisterTypes
from fabrication import VectorRegisterBlueprint
from register import VectorRegister
from transit import VectorRegisterCarrier


@dataclass(frozen=True)
class VectorRegisterTypes(RegisterTypes):
    model: Type[VectorRegister] = VectorRegister
    carrier: Type[VectorRegisterCarrier] = VectorRegisterCarrier
    blueprint: Type[VectorRegisterBlueprint] = VectorRegisterBlueprint