# src/toolkit/space/quadrant/southwest/toolkit.py

"""
Module: toolkit.space.quadrant.southwest.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from fabrication.blueprint.space.quadrant.southwest import SouthwestQuadrantBlueprint
from carrier import SouthwestQuadrantCarrier
from err import SouthwestQuadrantBlueprintNullException, SouthwestQuadrantCarrierNullException, SouthwestQuadrantNullException
from space import SouthwestQuadrant
from toolkit.geometry.space.quadrant.southwest.toolkit import QuadrantToolkit


@dataclass
class SouthwestQuadrantToolkit(QuadrantToolkit[SouthwestQuadrant]):
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
    model: Type[SouthwestQuadrant] = SouthwestQuadrant
    carrier_model: Type[SouthwestQuadrantCarrier] = SouthwestQuadrantCarrier
    blueprint_model: Type[SouthwestQuadrantBlueprint] = SouthwestQuadrantBlueprint
    
    null_exception: SouthwestQuadrantNullException = SouthwestQuadrantNullException()
    carrier_null_exception: SouthwestQuadrantCarrierNullException = SouthwestQuadrantCarrierNullException()
    blueprint_null_exception: SouthwestQuadrantBlueprintNullException = SouthwestQuadrantBlueprintNullException()

