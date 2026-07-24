# src/toolkit/space/vector/toolkit.py

"""
Module: toolkit.space.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import VectorSpaceBlueprint
from carrier.space.vector.carrier import VectorSpaceCarrier
from err import VectorSpaceBlueprintNullException, VectorSpaceCarrierNullException, VectorSpaceNullException
from suite import  CoordOperationSuite, VectorOperationSuite
from space import VectorSpace
from toolkit import SpaceToolkit


@dataclass
class VectorSpaceToolkit(SpaceToolkit[VectorSpace]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianVector tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[VectorSpace]
        blueprint_space: VectorSpaceBlueprint
        
        null_exception: VectorSpaceNullException
        blueprint_null_exception: VectorSpaceBlueprintNullException
        coord: CoordOperationSuite
        vector: VectorOperationSuite

    Provides:

    Super Class:
        SpaceToolkit
    """
    model: Type[VectorSpace] = (
        VectorSpace
    )
    blueprint_model: Type[VectorSpaceBlueprint] = (
        VectorSpaceBlueprint
    )
    carrier_model = Type[VectorSpaceCarrier] = (
        VectorSpaceCarrier
    )
    
    null_exception: VectorSpaceNullException = (
        VectorSpaceNullException()
    )
    carrier_null_exception: VectorSpaceCarrierNullException = (
        VectorSpaceCarrierNullException()
    )
    blueprint_null_exception: VectorSpaceBlueprintNullException = (
        VectorSpaceBlueprintNullException()
    )
    
    coord: CoordOperationSuite = CoordOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()

