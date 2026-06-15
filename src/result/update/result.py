# src/result/update/result.py

"""
Module: result.update.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from err import MethodImplementationException
from result import UpdateState

T = TypeVar("T")


class UpdateResult(Generic[T]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of an update

    Attributes:
        exception: Optional[Exception]
        payload: Optional[T]
        state: SearchState
        is_timed_out: bool
        is_success: bool
        is_failure: bool
        is_empty: bool

    Provides:
        -   def empty() -> SearchResult[T]:
        -   def success(payload: T) -> Result[T]
        -   def failure(exception: Exception) -> Result[T]
        -   def timed_out(cls, exception: Exception) -> SearchResult[T]:

    Super Class:
        Result
    """
    _state: UpdateState
    _original: Optional[T]
    _updated: Optional[T]
    _exception: Optional[Exception]

    def __init__(
            self,
            state: UpdateState,
            original: Optional[T],
            updated: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
        self._updated = updated
        self._original = original
        self._exception = exception
        
    @property
    def state(self) -> UpdateState:
        return self._state
        
    @property
    def original(self) -> T:
        return self._original
    
    @property
    def updated(self) -> Optional[T]:
        return self._updated
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def is_success(self) -> bool:
        return (
            self._original is not None and
            self._updated is not None and
            self._exception is None and
            self._state == UpdateState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self._updated is None and
                self.original is not None and
                self.exception is not None and
                self.state == UpdateState.FAILURE or
                self.state == UpdateState.TIMED_OUT
        )
    
    @property
    def is_nothing_to_update(self) -> bool:
        return (
                self._updated is None and
                self.original is not None and
                self.exception is None and
                self.state == UpdateState.ORIGINAL_AND_UPDATE_ARE_SAME
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self._updated is None and
                self.original is not None and
                self.exception is not None and
                self.state == UpdateState.TIMED_OUT
        )
    
    @classmethod
    def update_success(cls, original: T, updated: T) -> UpdateResult:
        return cls(
            updated=updated,
            original=original,
            exception=None,
            state=UpdateState.SUCCESS,
        )
    
    @classmethod
    def update_failure(cls, original: T, exception: Exception) -> UpdateResult:
        return cls(
            updated=None,
            original=original,
            exception=exception,
            state=UpdateState.FAILURE,
        )
    
    @classmethod
    def update_timed_out(cls, original: T, exception: Exception) -> UpdateResult:
        return cls(
            updated=None,
            original=original,
            exception=exception,
            state=UpdateState.TIMED_OUT,
        )
    
    @classmethod
    def nothing_to_update(cls, ) -> UpdateResult:
        method = f"{cls.__name__}.nothing_to_update"
        return cls(
            original=None,
            updated=None,
            exception=None,
            state=UpdateState.ORIGINAL_AND_UPDATE_ARE_SAME,
        )
    
    # @classmethod
    # def success(cls, payload: T) -> UpdateResult:
    #     return cls(
    #         updated=None,
    #         original=None,
    #         exception=MethodImplementationException(
    #             msg=f"{cls.__name__} does not implement the f{super.__name__}.success()"
    #                 f" method. Use the update_success() instead.",
    #             err_code=MethodImplementationException.ERR_CODE,
    #         ),
    #         state=UpdateState.CALLED_UNIMPLEMENTED_METHOD,
    #     )
    #
    # @classmethod
    # def failure(cls, exception: Exception) -> UpdateResult:
    #     return cls(
    #         updated=None,
    #         original=None,
    #         exception=MethodImplementationException(
    #             msg=f"{cls.__name__} does not implement the f{super.__name__}.failure()"
    #                 f"method. Use the update_failure() instead.",
    #             err_code=MethodImplementationException.ERR_CODE,
    #         ),
    #         state=UpdateState.CALLED_UNIMPLEMENTED_METHOD,
    #     )

    
