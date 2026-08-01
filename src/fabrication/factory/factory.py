# src/factory/__init__.py

"""
Module: factory/__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from result import BuildResult
from util import LoggingLevelRouter

T = TypeVar("T")


class Factory(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Creation process owners.
        2.  Assure objects comply with business logic at point of creation.
        3.  Ensure stateful data-holding factory resources satisfy contracts.
    
    Attributes:

    Provides:
        -   execute(*args, **kwargs) -> BuildResult[T]
        
    Super Class:
    """

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self,) -> BuildResult[T]:
        pass