# src/suite/suite.py

"""
Module: suite.suite
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from builder import Builder
from toolkit import ModelToolkit
from validator import Validator

T = TypeVar("T", bound="Model")



class ModelOperationSuite(ABC, Generic[T]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider
        
    Responsibilities:
        1.  Contains the operations that can be performed on a model.

    Attributes:
        toolkit: ModelToolkit[T]
    
    Provides:
        
    Super Class:
        Toolkit
        
    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: ModelToolkit[T]
    validator: Validator[T]
    builder: Builder[T]
