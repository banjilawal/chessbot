# src/toolkit/space/vector/toolkit.py

"""
Module: toolkit.space.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from blueprint import Blueprint
from carrier import EntityCarrier
from err import SpaceBlueprintNullException, SpaceCarrierNullException, SpaceNullException
from toolkit import Toolkit

T = TypeVar("T", bound="Space")

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
    model: Type[T]
    carrier_model: Type[EntityCarrier[T]]
    blueprint_model: Type[Blueprint[T]]
    
    null_exception: SpaceNullException = SpaceNullException()
    carrier_null_exception: SpaceCarrierNullException = SpaceNullException()
    blueprint_null_exception: SpaceBlueprintNullException = SpaceBlueprintNullException()

