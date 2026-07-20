# src/toolkit/model/state/toolkit.py

"""
Module: toolkit.model.state.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Type, TypeVar

from blueprint import Blueprint
from toggle.carrier import EntityCarrierToggle
from err import BlueprintNullException, EntityCarrierNullException, StateModelNullException
from toolkit import ModelToolkit

T = TypeVar("T", bound="StateModel")


class StateModelToolkit(ModelToolkit, Generic[T]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services a stateful model requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        model: StateModel
        
        blueprint_model: Blueprint
        carrier_model: DtoOperand

        null_exception: ModelNullException
        blueprint_null_exception: BlueprintNullException
        carrier_null_exception: DtoOperandNullException[T]

        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
       ModelToolkit

    Notes:
        -   ModelToolkit for an empty class which makes managing toolkits easier.
        -   Any toolkits for a model should be a ModelToolkit subclass.
    """
    model: Type[T]
    carrier_model: Type[EntityCarrierToggle[T]]
    blueprint_model: Type[Blueprint[T]]
    
    null_exception: StateModelNullException
    blueprint_null_exception: BlueprintNullException
    carrier_null_exception: EntityCarrierNullException
