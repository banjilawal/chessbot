# src/chess/system/data/operation/deletion/wrapper.py

"""
Module: chess.system.data.operation.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from chess.system import DataResult, DataResultEnum

T = TypeVar("T")


class DeletionResult(DataResult[Generic[T]]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a deletion to the caller.
    2.  Enforcing mutual exclusion. A DeletionResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    def __init__(
            self,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
            state: Optional[DataResultEnum] = None,
    ):
        super().__init__(
            state=state,
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "DeletionResult.wrapper"
    
    @property
    def is_success(self) -> bool:
        return (
                self.payload is not None and
                self.exception is None and
                self._state == DataResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == DataResultEnum.FAILURE
        )
    
    @property
    def is_nothing_to_delete(self) -> bool:
        return (
                self.payload is None and
                self.exception is None and
                self._state == DataResultEnum.NOTHING_TO_DELETE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state == DataResultEnum.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> DeletionResult[T]:
        return cls(
            payload=payload,
            exception=None,
            state=DataResultEnum.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=DataResultEnum.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=DataResultEnum.TIMED_OUT,
        )
    
    @classmethod
    def nothing_to_delete(cls) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=None,
            state=DataResultEnum.NOTHING_TO_DELETE,
        )

