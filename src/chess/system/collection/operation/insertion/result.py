# src/chess/system/data/result/insertion/result.py

"""
Module: chess.system.data.result.insertion.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar, cast

from chess.system import DataResult, DataResultEnum, InsertionResultState

T = TypeVar("T")

class InsertionResult(DataResult[T], Generic[T]):
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
                self.payload and
                self.exception is None and
                DataResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                not self.payload and
                self.exception is not None and
                DataResultEnum.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                not self.payload and
                self.exception is not None and
                DataResultEnum.TIMED_OUT
        )
    
    @classmethod
    def success(cls,) -> InsertionResult[T]:
        return cls(
            payload=True,
            exception=None,
            state=DataResultEnum.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> InsertionResult[T]:
        return cls(
            payload=False,
            exception=exception,
            state=DataResultEnum.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> InsertionResult[T]:
        return cls(
            payload=False,
            exception=exception,
            state=DataResultEnum.TIMED_OUT,
        )

