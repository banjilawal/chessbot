# src/operation/toolkit/space/axis/south/toolkit.py

"""
Module: operation.toolkit.space.axis.south.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain.metadata.blueprint.space import SouthAxisBlueprint
from carrier import SouthAxisCarrier
from err import SouthAxisBlueprintNullException, SouthAxisCarrierNullException, SouthAxisNullException
from space import SouthAxis
from operation.toolkit.geometry.space.axis.south.toolkit import AxisToolkit


@dataclass
class SouthAxisToolkit(AxisToolkit[SouthAxis]):
    """
    Role:
        -  Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianSpace tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        space: Type[T]
        blueprint_space: Blueprint[T]
        
        null_exception: SpaceNullException
        blueprint_null_exception: SpaceBlueprintNullException

    Provides:

    Super Class:
        Toolkit
    """
    model: Type[SouthAxis] = SouthAxis
    carrier_model: Type[SouthAxisCarrier] = SouthAxisCarrier
    blueprint_model: Type[SouthAxisBlueprint] = SouthAxisBlueprint
    
    null_exception: SouthAxisNullException = SouthAxisNullException()
    carrier_null_exception: SouthAxisCarrierNullException = SouthAxisCarrierNullException()
    blueprint_null_exception: SouthAxisBlueprintNullException = SouthAxisBlueprintNullException()

