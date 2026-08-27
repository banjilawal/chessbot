# src/operation/toolkit/space/quadrant/northeast/toolkit.py

"""
Module: operation.toolkit.space.quadrant.northeast.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain.metadata.blueprint.space.quadrant.northeast import NortheastQuadrantBlueprint
from carrier import NortheastQuadrantCarrier
from err import NortheastQuadrantBlueprintNullException, NortheastQuadrantCarrierNullException, NortheastQuadrantNullException
from space import NortheastQuadrant
from operation.toolkit.geometry.space.quadrant.northeast.toolkit import QuadrantToolkit


@dataclass
class NortheastQuadrantToolkit(QuadrantToolkit[NortheastQuadrant]):
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
    model: Type[NortheastQuadrant] = NortheastQuadrant
    carrier_model: Type[NortheastQuadrantCarrier] = NortheastQuadrantCarrier
    blueprint_model: Type[NortheastQuadrantBlueprint] = NortheastQuadrantBlueprint
    
    null_exception: NortheastQuadrantNullException = NortheastQuadrantNullException()
    carrier_null_exception: NortheastQuadrantCarrierNullException = NortheastQuadrantCarrierNullException()
    blueprint_null_exception: NortheastQuadrantBlueprintNullException = NortheastQuadrantBlueprintNullException()

