# src/toolkit/model/vector/toolkit.py

"""
Module: toolkit.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import VectorBlueprint
from carrier import VectorCarrier
from err import VectorBlueprintNullException, VectorCarrierNullException, VectorNullException
from model import Vector
from toolkit import ModelToolkit
from validator import NumberValidator


@dataclass
class VectorToolkit(ModelToolkit[Vector]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Vector tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[Vector]
        carrier_model: Type[VectorCarrier]
        blueprint_model: Type[VectorBlueprint]
        
        null_exception: VectorNullException
        carrier_null_exception: VectorCarrierNullException
        blueprint_null_exception: VectorBlueprintNullException
    
        number_validator: NumberValidator

    Provides:

    Super Class:
       ModelToolkit
    """
    model: Type[Vector] = Vector
    carrier_model: Type[VectorCarrier] = VectorCarrier
    blueprint_model: Type[VectorBlueprint] = VectorBlueprint
    
    null_exception: VectorNullException = VectorNullException()
    carrier_null_exception: VectorCarrierNullException = VectorCarrierNullException()
    blueprint_null_exception: VectorBlueprintNullException = VectorBlueprintNullException()

    number_validator: NumberValidator = NumberValidator()

    