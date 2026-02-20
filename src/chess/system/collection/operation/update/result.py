# src/chess/system/collection/operation/update/result.py

"""
Module: chess.system.collection.operation.update.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from chess.system import DataResult, UpdateResultEnum, UpdateResultState

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
    _updated: Optional[T]

    def __init__(
            self,
            original: T,
            state: UpdateResultState,
            exception: Optional[Exception] = None,
            updated: Optional[T] = None,
    ):
        super().__init__(state=state, payload=original, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "UpdateResult.result"
        self._updated = updated
        
    @property
    def original(self) -> T:
        return self.payload
    
    @property
    def updated(self) -> Optional[T]:
        return self._updated
    
    @property
    def is_success(self) -> bool:
        return (
                self._updated is not None and
                self.original is not None and
                self.exception is None and
                self.state == UpdateResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self._updated is None and
                self.original is not None and
                self.exception is not None and
                self.state == UpdateResultEnum.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self._updated is None and
                self.original is not None and
                self.exception is not None and
                self.state == UpdateResultEnum.TIMED_OUT
        )
    
    # @property
    # def original_is_update(self) -> bool:
    #     return (
    #             self._update is None and self.exception is not None and
    #             self.original == self._update and
    #             self.exception is not None and
    #             self._state == UpdateResultEnum.ORIGINAL_IS_UPDATE
    #     )
    
    @classmethod
    def update_success(cls, original: T, updated: T) -> UpdateResult[T]:
        return cls(
            updated=updated,
            original=original,
            exception=None,
            state=UpdateResultState(classification=UpdateResultEnum.SUCCESS),
        )
    
    @classmethod
    def update_failure(cls, original: T, exception: Exception):
        return cls(
            updated=None,
            original=original,
            exception=exception,
            state=UpdateResultState(classification=UpdateResultEnum.FAILURE),
        )
    
    @classmethod
    def update_timed_out(cls, original: T, exception: Exception):
        return cls(
            updated=None,
            original=original,
            exception=exception,
            state=UpdateResultState(classification=UpdateResultEnum.TIMED_OUT),
        )
