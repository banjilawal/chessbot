# src/toolkit/model/toolkit.py

"""
Module: toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Type, TypeVar

from blueprint import Blueprint
from toggle.carrier import EntityCarrierToggle
from err import BlueprintNullException, EntityCarrierNullException, ModelNullException
from toolkit import Toolkit

T = TypeVar("T", bound="Model")



class ModelToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider
        
    Responsibilities:
        1.  Aggregates workers and services a model requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        model: Type[T]
        carrier_model: Type[EntityCarrier[T]]
        blueprint_model: Type[Blueprint[T]]
        
        null_exception: ModelNullException
        blueprint_null_exception: BlueprintNullException
        carrier_null_exception: EntityCarrierNullException
        
    Provides:
        
    Super Class:
       Toolkit
    """
    model: Type[T]
    carrier_model: Type[EntityCarrierToggle[T]]
    blueprint_model: Type[Blueprint[T]]
    
    null_exception: ModelNullException
    blueprint_null_exception: BlueprintNullException
    carrier_null_exception: EntityCarrierNullException
    


