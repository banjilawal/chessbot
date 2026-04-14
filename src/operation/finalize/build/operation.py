# src/operation/finalize/finalizer.py

"""
Module: operation.finalize.finalizer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TypeVar

from model import Blueprint
from operation import Finalizer
from result import BuildResult
from system import LoggingLevelRouter

T = TypeVar("T")

class AssemblyFinalizer(Finalizer[T]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            product: T,
            blueprint: Blueprint[T],
            *args,
            **kwargs
    ) -> BuildResult[T]:
        pass