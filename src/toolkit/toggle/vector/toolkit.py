# src/toolkit/toggle/vector/toolkit.py

"""
Module: toolkit.toggle.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import VectorToggleBlueprint
from carrier.toggle.vector.toggle import VectorToggleCarrier
from err import VectorToggleNullException
from suite import  CoordOperationSuite, VectorOperationSuite
from toggle import VectorToggle
from toolkit import ToggleToolkit


@dataclass
class VectorToggleToolkit(ToggleToolkit[VectorToggle]):
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
    model: Type[VectorToggle] = VectorToggle
    blueprint_toggle: Type[VectorToggleBlueprint] = VectorToggleBlueprint
    carrier_model = Type[VectorToggleCarrier] = VectorToggleCarrier
    
    null_exception: VectorToggleNullException = VectorToggleNullException()
    blueprint_null_exception: VectorToggleBlueprintNullException = VectorToggleBlueprintNullException()
    
    coord: CoordOperationSuite = CoordOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()

