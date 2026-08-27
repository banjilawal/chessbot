# src/operation/toolkit/toggle/vector/toolkit.py

"""
Module: operation.toolkit.toggle.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain.metadata.blueprint import CartesianToggleBlueprint
from carrier.toggle.vector.carrier import CartesianToggleCarrier
from err import CartesianToggleBlueprintNullException, CartesianToggleCarrierNullException, CartesianToggleNullException
from operation.suite import  CoordOperationSuite, VectorOperationSuite
from domain.structure.toggle import CartesianToggle
from operation.toolkit.toggle.vector.toolkit import ToggleToolkit


@dataclass
class CartesianToggleToolkit(ToggleToolkit[CartesianToggle]):
    """
    Role:
        - Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianVector tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[CartesianToggle]
        blueprint_toggle: CartesianToggleBlueprint
        
        null_exception: CartesianToggleNullException
        blueprint_null_exception: CartesianToggleBlueprintNullException
        coord: CoordOperationSuite
        vector: VectorOperationSuite

    Provides:

    Super Class:
        ToggleToolkit
    """
    model: Type[CartesianToggle] = (
        CartesianToggle
    )
    blueprint_model: Type[CartesianToggleBlueprint] = (
        CartesianToggleBlueprint
    )
    carrier_model = Type[CartesianToggleCarrier] = (
        CartesianToggleCarrier
    )
    
    null_exception: CartesianToggleNullException = (
        CartesianToggleNullException()
    )
    carrier_null_exception: CartesianToggleCarrierNullException = (
        CartesianToggleCarrierNullException()
    )
    blueprint_null_exception: CartesianToggleBlueprintNullException = (
        CartesianToggleBlueprintNullException()
    )
    
    coord: CoordOperationSuite = CoordOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()

