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
from err import BlueprintNullException, DtoOperandNullException, ModelNullException, NullException
from microservice import IdentityService
from operand import DtoOperand
from toolkit import Toolkit
from validator import BlueprintIdExtractor

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
        model: T
        blueprint_model: Blueprint[T]
        identity_service: IdentityService
        priming_validator: PrimingValidator
        blueprint_id_validator: BlueprintIdValidator
        null_exception: ModelNullException
        blueprint_null_exception: BlueprintNullException
        
    Provides:
        
    Super Class:
       ModelToolkit
        
    Notes:
        -   ModelToolkit for an empty class which makes managing toolkits easier.
        -   Any toolkits for a model should be a ModelToolkit subclass.
    """
    """
    Args:
        model: Type[T]
        operand_model: Type[DtoOperand[T]]
        blueprint_model: Type[Blueprint[T]]

        null_exception: ModelNullException
        blueprint_null_exception: BlueprintNullException
        operand_null_exception: DtoOperandNullException
        
        identity_service: IdentityService
        priming_validator: PrimingValidator
    """
    model: Type[T]
    operand_model: Type[DtoOperand[T]]
    blueprint_model: Type[Blueprint[T]]
    
    null_exception: ModelNullException
    blueprint_null_exception: BlueprintNullException
    operand_null_exception: DtoOperandNullException
    
    identity_service: IdentityService = IdentityService()

