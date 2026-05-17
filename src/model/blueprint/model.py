# src/model/blueprint/model.py

"""
Module: model.blueprint.model
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
        1.  Provides values for instantiating a T object.
    
    Attributes:
    
    Provides:
    
    Super Class:
    """
    model_type: T
    null_exception: NullException = NullException()