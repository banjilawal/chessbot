# src/operation/suite/detector/suite.py

"""
Module: kit.detector.suite.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar

from kit import Suite

T = TypeVar("T", bound="StateModel")



class SensorSuite(Suite, Generic[T]):
    """
    Role:
        - Dependency Container
        -  Dynamic Dependency Provider
        
    Responsibilities:
        1.  Contains the operations that can be performed on a model.

    Attributes:
        toolkit: ModelToolkit[T]
    
    Provides:
        
    Super Class:
        Toolkit
        
    Notes:
        -  Suite for an empty class which makes managing toolkits easier.
        -  Any toolkits for a suite should be a Suite subclass.
    """
    
