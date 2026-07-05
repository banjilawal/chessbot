# src/toolkit/model/toolkit.py

"""
Module: toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from err import NullException
from microservice import IdentityService
from toolkit import Toolkit
from validation import BlueprintIdValidator

T = TypeVar("T")



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
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []
        
        identity_service: IdentityService
        priming_validator: PrimingValidator
        blueprint_id_validator: BlueprintIdValidator
        
        _entries: Dict[str, Any]
    
    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:
        -   def _resolve_service_dependencies() -> SearchResult[List[Dict[str, Microservice]]]:
        -   def _resolve_dependencies(self) -> SearchResult[List[Dict[str, Operation]]]
        
    Super Class:
       ModelToolkit
        
    Notes:
        -   ModelToolkit for an empty class which makes managing toolkits easier.
        -   Any toolkits for a model should be a ModelToolkit subclass.
    """
    model: T
    null_exception: NullException
    identity_service: IdentityService = IdentityService()
    blueprint_id_validator: BlueprintIdValidator = BlueprintIdValidator()
