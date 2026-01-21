# src/chess/system/data/result/update/result.py

"""
Module: chess.system.data.result.update.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar, cast

from chess.system import (
    DataResult, DataResultState, UpdateResult
)

T = TypeVar("T")


class UpdateResult(DataResult[T], Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a update to the caller.
    2.  Enforcing mutual exclusion. A UpdateResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (DataResultState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    def __init__(
            self,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
            state: Optional[DataResultState] = None,
    ):
        super().__init__(
            state=state,
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "UpdateResult.__init__"
    
    @property
    def is_success(self) -> bool:
        return (
                self.payload is not None and
                self.exception is None and
                self._state == DataResultState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == DataResultState.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == DataResultState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> UpdateResult[T]:
        return cls(
            payload=payload,
            exception=None,
            state=DataResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> UpdateResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=DataResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> UpdateResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=DataResultState.TIMED_OUT,
        )
    
    @classmethod
    def empty(cls) -> UpdateResult[T]:
        return cls(
            payload=None,
            exception=None,
            state=DataResultState.EMPTY,
        )