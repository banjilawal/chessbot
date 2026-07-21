# src/toolkit/model/scalar/toolkit.py

"""
Module: toolkit.model.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import ScalarBlueprint
from carrier import ScalarCarrierToggle
from err import ScalarBlueprintNullException, ScalarCarrierNullException, ScalarNullException
from model import Scalar
from toolkit import ModelToolkit
from validator import NumberValidator


@dataclass
class ScalarToolkit(ModelToolkit[Scalar]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Scalar tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[Scalar]
        carrier_model: Type[ScalarCarrier]
        blueprint_model: Type[ScalarBlueprint]
        
        null_exception: ScalarNullException
        carrier_null_exception: ScalarCarrierNullException
        blueprint_null_exception: ScalarBlueprintNullException
    
        number_validator: NumberValidator

    Provides:

    Super Class:
       ModelToolkit
    """
    model: Type[Scalar] = Scalar
    carrier_model: Type[ScalarCarrierToggle] = ScalarCarrierToggle
    blueprint_model: Type[ScalarBlueprint] = ScalarBlueprint
    
    null_exception: ScalarNullException = ScalarNullException()
    carrier_null_exception: ScalarCarrierNullException = ScalarCarrierNullException()
    blueprint_null_exception: ScalarBlueprintNullException = ScalarBlueprintNullException()

    number_validator: NumberValidator = NumberValidator()

    