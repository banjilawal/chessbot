# src/build/build.py

"""
Module: build/build
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from assembler import Assembler
from blueprint import Blueprint
from result import BuildResult
from err.root import RootCertifier
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
        root_certifier: RootCertifier[T]

    Provides:
        -   def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]
        
    Super Class:
    """
    _bootstrapper: RootCertifier[T]
    _assembler: Assembler[T]
    
    def __init__(
            self, bootstrapper: RootCertifier[T], assembler: Assembler[T],
    ):
        """
        Args:
            bootstrapper: RootCertifier[T]
            assembler: Assembler[T]
            
        """
        self._bootstrapper = bootstrapper
        self._assembler =assembler
    
    @property
    def bootstrapper(self) -> RootCertifier[T]:
        return cast(RootCertifier[T], self._bootstrapper)
    
    @property
    def assembler(self) -> Assembler[T]:
        return cast(Assembler[T], self._assembler)

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
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