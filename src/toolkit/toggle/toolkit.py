# src/toolkit/toggle/vector/toolkit.py

"""
Module: toolkit.toggle.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from blueprint import Blueprint
from toggle import EntityCarrierToggle, Toggle
from toolkit import Toolkit

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
    carrier_model: Type[EntityCarrierToggle[T]]
    blueprint_model: Type[Blueprint[T]]
    
    null_exception: ToggleNullException = ToggleNullException()
    blueprint_null_exception: ToggleBlueprintNullException = ToggleBlueprintNullException()

