# src/chess/system/collectionoperation/computation/result.py

"""
Module: chess.system.collection.operation.computation.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from chess.system import DataResult, DataResultEnum, UnsupportedEmptyComputationResultException
from chess.system.collection.operation.computation.state.state import ComputationResultState

T = TypeVar("T")

class ComputationResult(DataResult[T], Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a calculation to the caller.
    2.  Enforcing mutual exclusion. A ComputationResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (DataResultEnum)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    
    def __init__(
            self,
            state: ComputationResultState,
            exception: Optional[Exception] = None,
            payload: Optional[T] = None,
    ):
        super().__init__(state=state, payload=payload, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "ComputationResult.result"

    @property
    def is_success(self) -> bool:
        return (
                self.payload is not None and
                self.exception is None and
                self.state.classification == DataResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state.classification == DataResultEnum.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state == DataResultEnum.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> ComputationResult[T]:
        return cls(
            payload=payload,
            exception=None,
            state=ComputationResultState(state=DataResultEnum.SUCCESS),
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ComputationResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=ComputationResultState(state=DataResultEnum.FAILURE),
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ComputationResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=ComputationResultState(state=DataResultEnum.TIMED_OUT),
        )

    

    



