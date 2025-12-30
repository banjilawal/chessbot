# src/chess/system/build/builder/builder.py

"""
Module: chess.system.build.builder.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import BuildResult, LoggingLevelRouter, Validator

T = TypeVar("T")


class Builder(ABC, Generic[T]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor,

    # RESPONSIBILITIES:
    1.  Produce objects whose integrity is guaranteed at creation.
    2.  Manage construction of objects that can be used safely by the client.
    3.  Ensure resources for building a object have met the application's safety contracts.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    def builder(self):
        pass
    
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