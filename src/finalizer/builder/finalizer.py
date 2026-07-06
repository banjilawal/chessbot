# src/finalizer/builder/finalizer.py

"""
Module: finalizer.builder.finalizer
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
from util import LoggingLevelRouter

T = TypeVar("T")

class BuilderFinalizer(Finalizer[T]):
    
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