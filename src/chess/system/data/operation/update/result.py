# src/chess/system/data/operation/update/result.py

"""
Module: chess.system.data.operation.update.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""
from abc import abstractmethod
from typing import Generic, Optional, TypeVar

from chess.system import DTO, DataResult, DataResultEnum, UpdateResult

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
        *   state (DataResultEnum)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    _current: T

    def __init__(
            self,
            previous_data: DTO,
            current:  Optional[T],
            exception: Optional[Exception] = None,
            state: Optional[DataResultEnum] = None,
    ):
        super().__init__(
            state=state,
            payload=previous_data,
            exception=exception
        )
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "UpdateResult.result"
        self._current = current
        
    @property
    def previous(self) -> T:
        return self.payload
    
    @property
    def current(self) -> Optional[T]:
        return self._current
    
    @property
    def is_success(self) -> bool:
        return (
                self._current is not None and
                self.previous is not None and
                self.exception is None and
                self._state == DataResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self._current is None and
                self.previous is not None and
                self.exception is not None and
                self.state == DataResultEnum.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self._current is None and
                self.previous is not None and
                self.exception is not None and
                self.state == DataResultEnum.TIMED_OUT
        )
    
    @property
    def are_the_same(self) -> bool:
        return (
                self._current is None and self.exception is not None and
                self.previous == self._current and
                self.exception is not None and
                self._state == DataResultEnum.CURRENT_AND_PREVIOUS_THE_SAME
        )
    
    @classmethod
    def update_success(cls, previous: T, current: T) -> UpdateResult[T]:
        return cls(
            previous=previous,
            current=current,
            exception=None,
            state=DataResultEnum.SUCCESS,
        )
    
    @classmethod
    def update_failure(cls, previous: T, current: T, exception: Exception):
        return cls(
            previous=previous,
            current=current,
            exception=exception,
            state=DataResultEnum.FAILURE,
        )
    
    @classmethod
    def update_timed_out(cls, previous: T, current: T, exception: Exception):
        return cls(
            previous=previous,
            current=current,
            exception=exception,
            state=DataResultEnum.TIMED_OUT,
        )
    
    @classmethod
    def nothing_to_change(cls, previous: T, current: T) -> UpdateResult[T]:
        return cls(
            previous=previous,
            current=current,
            exception=None,
            state=DataResultEnum.CURRENT_AND_PREVIOUS_THE_SAME,
        )
    
    @classmethod
    def empty(cls) -> UpdateResult[T]:
        return cls(
            previous=None,
            current=None,
            exception=None,
            state=DataResultEnum.EMPTY,
        )