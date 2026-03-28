# src/logic/system/build/build/exception.py

"""
Module: logic.system.build.build.build
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from logic.system import BuildResult, LoggingLevelRouter, ValidationProcess

T = TypeVar("T")


class BuildProcess(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Creation process owners.
        2.  Execute binding logic for related entities.
        3.  Assure objects comply with business logic at point of creation.
        4.  Ensure stateful data-holding build resources meet satisfy contracts.
    
    Attributes:

    Provides:
        -   execute(*args, **kwargs) -> BuildResult[T]
        
    Super Class:
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs) -> BuildResult[T]:
        pass