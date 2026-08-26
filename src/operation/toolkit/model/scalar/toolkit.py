# src/operation/toolkit/model/scalar/toolkit.py

"""
Module: operation.toolkit.model.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain.metadata.blueprint import ScalarBlueprint
from carrier import ScalarCarrier
from err import ScalarBlueprintNullException, ScalarCarrierNullException, ScalarNullException
from domain.model import Scalar
from operation.toolkit.model.scalar.toolkit import ModelToolkit
from transit.dispatcher.validator import NumberValidator


@dataclass
class ScalarToolkit(ModelToolkit[Scalar]):
    """
    Role:
        -  Container
    
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
    carrier_model: Type[ScalarCarrier] = ScalarCarrier
    blueprint_model: Type[ScalarBlueprint] = ScalarBlueprint
    
    null_exception: ScalarNullException = ScalarNullException()
    carrier_null_exception: ScalarCarrierNullException = ScalarCarrierNullException()
    blueprint_null_exception: ScalarBlueprintNullException = ScalarBlueprintNullException()

    number_validator: NumberValidator = NumberValidator()

    