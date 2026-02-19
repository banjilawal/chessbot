# src/chess/system/collection/result/insertion/result.py

"""
Module: chess.system.collection.result.insertion.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional, TypeVar

from chess.system import DataResult, InsertionResultEnum, InsertionResultState

class InsertionResult(DataResult[bool]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a insertion to the caller.
    2.  Enforcing mutual exclusion. A InsertionResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (InsertionState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    def __init__(
            self,
            payload: bool,
            state: InsertionResultState,
            exception: Optional[Exception] = None,
    ):
        super().__init__(state=state, payload=payload, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "InsertionResult.__init__"
        
    @property
    def is_success(self) -> bool:
        return (
                self.payload == True and
                self.exception is None and
                self.state.classification == InsertionResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload == False and
                self.exception is not None and
                self.state.classification == InsertionResultEnum.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload == False and
                self.exception is not None and
                self.state.classification == InsertionResultEnum.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: bool = True) -> InsertionResult[bool]:
        return cls(
            payload=True,
            exception=None,
            state=InsertionResultState(InsertionResultEnum.SUCCESS),
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> InsertionResult[bool]:
        return cls(
            payload=False,
            exception=exception,
            state=InsertionResultState(InsertionResultEnum.FAILURE),
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> InsertionResult[bool]:
        return cls(
            payload=False,
            exception=exception,
            state=InsertionResultState(InsertionResultEnum.TIMED_OUT),
        )

