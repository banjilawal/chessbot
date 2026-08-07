# src/operation/tree/__init__.py

"""
Module: operation.tree.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from operation import Operation
from result import Result
from util import LoggingLevelRouter

T = TypeVar("T", bound="Chain")

class ChainOperation(Operation, ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Executes a task on a data-holding object or collection of data-holders.
        2.  The task produces a work product encapsulated in a Result object.

    Attributes:
        DOMAIN = "operation"
        OPERATION_NAME = "operation"

    Provides:
        -   def domains(self) -> List[str]:

    Super Class:
    """
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            operand: T,
            *args: Optional[tuple[Any, ...]],
            **kwargs: Optional[dict[str, Any]],
    ) -> Result[Any]:
        pass