# src/build/__init__.py

"""
Module: build/__init__
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


class Builder(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Creation process owners.
        2.  Assure objects comply with business logic at point of creation.
        3.  Ensure stateful data-holding build resources satisfy contracts.
    
    Attributes:

    Provides:
        -   build(*args, **kwargs) -> BuildResult[T]
        
    Super Class:
    """
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def build(cls, *args, **kwargs) -> BuildResult[T]:
        """
        # ACTION:
        1. Run integrity checks on each parameter required for constructing V.
        2. If any check fails it raises an exception that is returned inside a BuildResult.
        3. When all checks pass, construct V then return it inside a BuildResult.

        # PARAMETERS:
            * args: Parameters for constructing V.

        # RETURNS:
        BuildResult[V] containing either:
            - On success: V in the payload.
            - On failure: Exception.

        # RAISES:
          * BuildFailedException
        """
        pass