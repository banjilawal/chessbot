# src/chess/system/collection/operation/update/result.py

"""
Module: chess.system.collection.operation.update.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from platform import python_revision
from typing import Generic, Optional, TypeVar

from chess.system import DTO, DataResult, UpdateResultEnum, UpdateResultState

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
    _updated_entity: T

    def __init__(
            self,
            original_data: JSONObject,
            state: UpdateResultState,
            exception: Optional[Exception] = None,
            updated_entity: Optional[T] = None,
    ):
        super().__init__(state=state, payload=updated_entity, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "UpdateResult.result"
        self._original_data = original_data
        
    @property
    def previous(self) -> T:
        return self.payload
    
    @property
    def update(self) -> Optional[T]:
        return self.payload
    
    @property
    def is_success(self) -> bool:
        return (
                self._update is not None and
                self.previous is not None and
                self.exception is None and
                self.state == UpdateResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self._update is None and
                self.previous is not None and
                self.exception is not None and
                self.state == UpdateResultEnum.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self._update is None and
                self.previous is not None and
                self.exception is not None and
                self.state == UpdateResultEnum.TIMED_OUT
        )
    
    @property
    def original_is_update(self) -> bool:
        return (
                self._update is None and self.exception is not None and
                self.previous == self._update and
                self.exception is not None and
                self._state == UpdateResultEnum.ORIGINAL_IS_UPDATE
        )
    
    @classmethod
    def update_success(cls, original: T, update: DTO) -> UpdateResult[T]:
        return cls(
            original=original,
            update=update,
            exception=None,
            state=UpdateResultState(classification=UpdateResultEnum.SUCCESS),
        )
    
    @classmethod
    def update_failure(cls, original: T, exception: Exception):
        return cls(
            original=original,
            update=None,
            exception=exception,
            state=UpdateResultState(classification=UpdateResultEnum.FAILURE),
        )
    
    @classmethod
    def update_timed_out(cls, original: T, exception: Exception):
        return cls(
            original=original,
            update=None,
            exception=exception,
            state=UpdateResultState(classification=UpdateResultEnum.TIMED_OUT),
        )
    
    @classmethod
    def original_same_as_update(cls, original: T, update: DTO) -> UpdateResult[T]:
        return cls(
            original=original,
            update=update,
            exception=None,
            state=UpdateResultState(classification=UpdateResultEnum.ORIGINAL_AND_UPDATE_ARE_SAME),
        )
