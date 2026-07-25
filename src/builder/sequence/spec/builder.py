# src/sequence/spec/spec.py

"""
Module: sequence.spec.spec
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from builder import Builder
from util import LoggingLevelRouter

T = TypeVar("T", bound="SequenceSpec")


class SequenceSpecBuilder(Builder, Generic[T]):
    """
    Role:
        -   Computation
        -   Iterator

    Responsibilities:
        1.  Provide a recurrence relation for iterating through a Space.

    Attributes:

    Provides:

    Super Class:
    """
    def __init__(self, builder_toolkit: SequenceSpecBuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)


    @property
    def builder_toolkit(self) -> SequenceSpecBuilderToolkit[T]:
        return cast(SequenceSpecBuilderToolkit[T], super().__init__())
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SequenceSpecBlueprint[T]) -> T:
        pass