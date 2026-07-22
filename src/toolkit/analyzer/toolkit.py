# src/toolkit/analyzer/toolkit.py

"""
Module: toolkit.analyzer.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import TypeVar

from err import NullException
from toolkit import Toolkit

T = TypeVar("T")



class AnalyzerToolkit(Toolkit[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Aggregates workers and services a analyzer requires for its tasks.
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
        -   AnalyzerToolkit for an empty class which makes managing toolkits easier.
        -   Any toolkits for a analyzer should be a AnalyzerToolkit subclass.
    """
