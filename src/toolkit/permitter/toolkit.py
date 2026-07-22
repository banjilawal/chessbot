# src/toolkit/permitter/toolkit.py

"""
Module: toolkit.permitter.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from permitter import Permitter
from toolkit import Toolkit

P = TypeVar("P", bound=Permitter)


class PermitterToolkit(Toolkit[Permitter, Generic[P]]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Aggregates workers and services a permitter requires for its tasks.
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
        Toolkit
        
    Notes:
        -   PermitterToolkit for an empty class which makes managing toolkits easier.
        -   Any toolkits for a permitter should be a PermitterToolkit subclass.
    """
