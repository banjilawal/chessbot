# src/toolkit/space/axis/north/toolkit.py

"""
Module: toolkit.space.axis.north.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from blueprint.space.axis.north import NorthAxisBlueprint
from carrier import NorthAxisCarrier
from err import NorthAxisBlueprintNullException, NorthAxisCarrierNullException, NorthAxisNullException
from space import NorthAxis
from toolkit import AxisToolkit


@dataclass
class NorthAxisToolkit(AxisToolkit[NorthAxis]):
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
    model: Type[NorthAxis] = NorthAxis
    carrier_model: Type[NorthAxisCarrier] = NorthAxisCarrier
    blueprint_model: Type[NorthAxisBlueprint] = NorthAxisBlueprint
    
    null_exception: NorthAxisNullException = NorthAxisNullException()
    carrier_null_exception: NorthAxisCarrierNullException = NorthAxisCarrierNullException()
    blueprint_null_exception: NorthAxisBlueprintNullException = NorthAxisBlueprintNullException()

