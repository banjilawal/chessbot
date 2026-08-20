# src/toolkit/toggle/vector/toolkit.py

"""
Module: toolkit.toggle.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from fabrication.blueprint import Blueprint
from carrier import EntityCarrier
from err import ToggleBlueprintNullException, ToggleCarrierNullException, ToggleNullException
from toolkit.toggle.toolkit import Toolkit

T = TypeVar("T", bound="Toggle")

@dataclass
class ToggleToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianVector tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        toggle: Type[T]
        blueprint_toggle: Blueprint[T]
        
        null_exception: ToggleNullException
        blueprint_null_exception: ToggleBlueprintNullException

    Provides:

    Super Class:
        Toolkit
    """
    model: Type[T]
    carrier_model: Type[EntityCarrier[T]]
    blueprint_model: Type[Blueprint[T]]
    
    null_exception: ToggleNullException = ToggleNullException()
    carrier_null_exception: ToggleCarrierNullException = ToggleNullException()
    blueprint_null_exception: ToggleBlueprintNullException = ToggleBlueprintNullException()

