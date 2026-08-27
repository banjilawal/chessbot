# src/operation/toolkit/space/quadrant/northwest/toolkit.py

"""
Module: operation.toolkit.space.quadrant.northwest.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain.metadata.blueprint.space.quadrant.northwest import NorthwestQuadrantBlueprint
from carrier import NorthwestQuadrantCarrier
from err import NorthwestQuadrantBlueprintNullException, NorthwestQuadrantCarrierNullException, NorthwestQuadrantNullException
from space import NorthwestQuadrant
from operation.toolkit.geometry.space.quadrant.northwest.toolkit import QuadrantToolkit


@dataclass
class NorthwestQuadrantToolkit(QuadrantToolkit[NorthwestQuadrant]):
    """
    Role:
        - Container

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
    model: Type[NorthwestQuadrant] = NorthwestQuadrant
    carrier_model: Type[NorthwestQuadrantCarrier] = NorthwestQuadrantCarrier
    blueprint_model: Type[NorthwestQuadrantBlueprint] = NorthwestQuadrantBlueprint
    
    null_exception: NorthwestQuadrantNullException = NorthwestQuadrantNullException()
    carrier_null_exception: NorthwestQuadrantCarrierNullException = NorthwestQuadrantCarrierNullException()
    blueprint_null_exception: NorthwestQuadrantBlueprintNullException = NorthwestQuadrantBlueprintNullException()

