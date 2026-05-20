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

from err import NullException

T = TypeVar("T")

class Blueprint(ABC, Generic[T]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Aggregates properties, values, entities that are passed to a method.
        2.  Simplify entry points to Provides values for instantiating a T object.
    
    Attributes:
        model_type: T
        null_exception: NullException
        
    Provides:
    
    Super Class:
    """
    model_type: T
    null_exception: NullException = NullException()