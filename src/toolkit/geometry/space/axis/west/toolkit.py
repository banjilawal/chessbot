# src/toolkit/space/axis/west/toolkit.py

"""
Module: toolkit.space.axis.west.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from fabrication.blueprint.space.axis.west import WestAxisBlueprint
from carrier import WestAxisCarrier
from err import WestAxisBlueprintNullException, WestAxisCarrierNullException, WestAxisNullException
from space import WestAxis
from toolkit.geometry.space.axis.west.toolkit import AxisToolkit


@dataclass
class WestAxisToolkit(AxisToolkit[WestAxis]):
    """
    Role:
        -   Container

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
    model: Type[WestAxis] = WestAxis
    carrier_model: Type[WestAxisCarrier] = WestAxisCarrier
    blueprint_model: Type[WestAxisBlueprint] = WestAxisBlueprint
    
    null_exception: WestAxisNullException = WestAxisNullException()
    carrier_null_exception: WestAxisCarrierNullException = WestAxisCarrierNullException()
    blueprint_null_exception: WestAxisBlueprintNullException = WestAxisBlueprintNullException()

