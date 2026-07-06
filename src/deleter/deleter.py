# src/deleter/deleter.py

"""
Module: deleter.deleter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import ABC
from typing import Generic, TypeVar


from result import DeletionResult
from stack import StackService
from util import LoggingLevelRouter

T = TypeVar("T")

class Deleter(ABC, Generic[T]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            item_id: int,
            stack: StackService[T],
            *args,
            **kwargs,
    ) -> DeletionResult[T]:
        pass