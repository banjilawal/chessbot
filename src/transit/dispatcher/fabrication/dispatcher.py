# src/transit/dispatcher/fabrication/validator.py

"""
Module: transit.dispatcher.fabrication.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from assurance import Validator
from artifcat import BuildResult
from transit import Dispatcher
from util import LoggingLevelRouter


T = TypeVar("T")


class BuildDispatcher(Dispatcher[BuildResult], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the Build workflow.

    Attributes:
        validator: Validator[T]

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[T]

    Super Class:
        Dispatcher
    """
    _validator: Validator[T]
    
    def __init__(self, validator: Validator[T]):
        """
        Args:
            validator: Validator[T]
        """
        self._validator = validator
        
    @property
    def validator(self) -> Validator[T]:
        return self._validator

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[T]:
        """
        Verify a candidate is safe to use.
        Args:
            job: Any
        Returns:
            BuildResult[T]
        Raises:
            ModelDispatcherException
        """
        pass
