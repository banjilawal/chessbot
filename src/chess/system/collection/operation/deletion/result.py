# src/chess/system/collection/operation/deletion/wrapper.py

"""
Module: chess.system.collection.operation.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from chess.system import DataResult, DeletionResultEnum
from chess.system.collection.operation.deletion.state.state import DeletionResultState

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
            state: DeletionResultState,
            exception: Optional[Exception] = None,
            payload: Optional[T] = None,
    ):
        super().__init__(state=state, payload=payload, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "DeletionResult.wrapper"
    
    @property
    def is_success(self) -> bool:
        return (
                self.payload is not None and
                self.exception is None and
                self.state.classification == DeletionResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state.classification == DeletionResultEnum.FAILURE
        )
    
    @property
    def is_nothing_to_delete(self) -> bool:
        return (
                self.payload is None and
                self.exception is None and
                self.state.classification == DeletionResultEnum.NOTHING_TO_DELETE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state.classification == DeletionResultEnum.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> DeletionResult[T]:
        return cls(
            payload=payload,
            exception=None,
            state=DeletionResultState(DeletionResultEnum.SUCCESS),
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=DeletionResultState(DeletionResultEnum.FAILURE),
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=DeletionResultState(DeletionResultEnum.TIMED_OUT),
        )
    
    @classmethod
    def nothing_to_delete(cls) -> DeletionResult[T]:
        return cls(
            payload=None,
            exception=None,
            state=DeletionResultState(DeletionResultEnum.NOTHING_TO_DELETE),
        )

