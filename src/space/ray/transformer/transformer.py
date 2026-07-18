# src/space/ray/computer/space/ray.py

"""
Module: space.ray.computer.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from container import TargetVectorSet
from result import ComputationResult
from util import LoggingLevelRouter
from validator import Validator

T = TypeVar("T", bound= "LinearSpace")


class LinearSpanTransformer(ABC, Generic[T]):
    """
    Role:
        -   Transformer
        -   Integrity assurance

    Responsibilities:
        1.  Produce a TargetVectorSet from an LinearSpace instead
            of a LinearVectorSet..


    Attributes:
        space: T
        validator: Validator[T]

    Provides:
        -   def execute() -> ComputationResult[TargetVectorSet]
        
    Super Class:
    """
    _linear_space: T
    _validator: Validator[T]
    
    def __init__(
            self,
            linear_space: T,
            validator: Validator[T]
    ):
        """
        Args:
            linear_space: T
            validator: Validator[T]
        """
        self._linear_space = linear_space
        self._validator = validator
    
    @property
    def linear_space(self) -> T:
        return self._linear_space
    
    @property
    def validator(self) -> Validator[T]:
        return self._validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self,) -> ComputationResult[TargetVectorSet]:
        pass