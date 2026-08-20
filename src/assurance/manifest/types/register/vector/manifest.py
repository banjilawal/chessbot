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


from fabrication import RegisterBlueprint
from register import Register
from transit import RegisterCarrier


@dataclass(frozen=True)
class VectorRegisterTypes(RegisterTypes[VectorRegister]):
    model: Type[Register] = Register
    carrier: Type[RegisterCarrier] = RegisterCarrier
    blueprint: Type[RegisterBlueprint] = RegisterBlueprint