# src/popper/operation.py

"""
Module: popper.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from typing import TypeVar

from operation import Operation
from result import DeletionResult
from stack import StackService
from util import LoggingLevelRouter

T = TypeVar("T")

class Popper(Operation[T]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            stack: StackService[T],
            *args,
            **kwargs,
    ) -> DeletionResult[T]:
        pass