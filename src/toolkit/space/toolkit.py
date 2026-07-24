# src/toolkit/space/vector/toolkit.py

"""
Module: toolkit.space.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Generic, Type

from blueprint import Blueprint, SpaceBlueprint
from carrier import EntityCarrier
from err import SpaceBlueprintNullException, SpaceCarrierNullException, SpaceNullException
from space import Space
from toolkit import Toolkit


@dataclass
class SpaceToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianVector tasks.
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
    model: Type[Space] = Space
    carrier_model: Type[SpaceCarrier]
    blueprint_model: Type[SpaceBlueprint] = SpaceBlueprint
    
    null_exception: SpaceNullException = SpaceNullException()
    carrier_null_exception: SpaceCarrierNullException = SpaceCarrierNullException()
    blueprint_null_exception: SpaceBlueprintNullException = SpaceBlueprintNullException()

