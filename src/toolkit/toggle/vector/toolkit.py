# src/toolkit/toggle/vector/toolkit.py

"""
Module: toolkit.toggle.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from fabrication.blueprint import VectorToggleBlueprint
from carrier.toggle.vector.carrier import VectorToggleCarrier
from err import VectorToggleBlueprintNullException, VectorToggleCarrierNullException, VectorToggleNullException
from suite import  CoordOperationSuite, VectorOperationSuite
from domain.toggle import CartesianToggle
from toolkit.toggle.vector.toolkit import ToggleToolkit


@dataclass
class VectorToggleToolkit(ToggleToolkit[CartesianToggle]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianVector tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[VectorToggle]
        blueprint_toggle: VectorToggleBlueprint
        
        null_exception: VectorToggleNullException
        blueprint_null_exception: VectorToggleBlueprintNullException
        coord: CoordOperationSuite
        vector: VectorOperationSuite

    Provides:

    Super Class:
        ToggleToolkit
    """
    model: Type[CartesianToggle] = (
        CartesianToggle
    )
    blueprint_model: Type[VectorToggleBlueprint] = (
        VectorToggleBlueprint
    )
    carrier_model = Type[VectorToggleCarrier] = (
        VectorToggleCarrier
    )
    
    null_exception: VectorToggleNullException = (
        VectorToggleNullException()
    )
    carrier_null_exception: VectorToggleCarrierNullException = (
        VectorToggleCarrierNullException()
    )
    blueprint_null_exception: VectorToggleBlueprintNullException = (
        VectorToggleBlueprintNullException()
    )
    
    coord: CoordOperationSuite = CoordOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()

