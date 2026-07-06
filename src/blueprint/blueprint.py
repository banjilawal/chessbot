# src/blueprint/blueprint.py

"""
Module: blueprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar


T = TypeVar("T")

class Blueprint(ABC, Generic[T]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating an object.
        2.  DTO
    
    Attributes:
        
    Provides:
    
    Super Class:
    """