# src/operation/toolkit/space/quadrant/southeast/toolkit.py

"""
Module: operation.toolkit.space.quadrant.southeast.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain.metadata.blueprint.space.quadrant.southeast import SoutheastQuadrantBlueprint
from carrier import SoutheastQuadrantCarrier
from err import SoutheastQuadrantBlueprintNullException, SoutheastQuadrantCarrierNullException, SoutheastQuadrantNullException
from space import SoutheastQuadrant
from operation.toolkit.geometry.space.quadrant.southeast.toolkit import QuadrantToolkit


@dataclass
class SoutheastQuadrantToolkit(QuadrantToolkit[SoutheastQuadrant]):
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
    model: Type[SoutheastQuadrant] = SoutheastQuadrant
    carrier_model: Type[SoutheastQuadrantCarrier] = SoutheastQuadrantCarrier
    blueprint_model: Type[SoutheastQuadrantBlueprint] = SoutheastQuadrantBlueprint
    
    null_exception: SoutheastQuadrantNullException = SoutheastQuadrantNullException()
    carrier_null_exception: SoutheastQuadrantCarrierNullException = SoutheastQuadrantCarrierNullException()
    blueprint_null_exception: SoutheastQuadrantBlueprintNullException = SoutheastQuadrantBlueprintNullException()

