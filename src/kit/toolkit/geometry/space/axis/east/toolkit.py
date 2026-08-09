# src/kit/toolkit/space/axis/east/toolkit.py

"""
Module: kit.toolkit.space.axis.east.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from fabrication.blueprint.space.axis.east import EastAxisBlueprint
from carrier import EastAxisCarrier
from err import EastAxisBlueprintNullException, EastAxisCarrierNullException, EastAxisNullException
from space import EastAxis
from kit.toolkit import AxisToolkit


@dataclass
class EastAxisToolkit(AxisToolkit[EastAxis]):
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
    model: Type[EastAxis] = EastAxis
    carrier_model: Type[EastAxisCarrier] = EastAxisCarrier
    blueprint_model: Type[EastAxisBlueprint] = EastAxisBlueprint
    
    null_exception: EastAxisNullException = EastAxisNullException()
    carrier_null_exception: EastAxisCarrierNullException = EastAxisCarrierNullException()
    blueprint_null_exception: EastAxisBlueprintNullException = EastAxisBlueprintNullException()

