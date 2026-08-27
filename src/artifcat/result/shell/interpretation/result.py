# src/artifact/result/shell/Interpretation/result.py

"""
Module: artfifact.result.shell.Interpretation.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Generic, Optional, TypeVar, cast

from artifcat import InterpretationState, ShellResult

T = TypeVar("T", bound="OperationRequest")

class InterpretationResult(ShellResult[T], Generic[T]):
    """
    Role:
        - Data Transport
        -  Error Transport

    Responsibilities:
        1.  Contains the outcome of an Interpretation.

    Attributes:
        exception: Optional[Exception]
        state: validationState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool
        is_nothing_to_interpret: bool

    Provides:
        -  def success(payload: T) -> InterpretationResu[T]
        -  def failure(exception: Exception) -> InterpretationResu[T]
        -  def timed_out(exception: Exception) -> InterpretationResult
        -  def nothing_to_interpret() -> InterpretationResult

    Super Class:
        Result
    """
    _state = InterpretationState
    
    def __init__(
            self,
            state: InterpretationState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            payload: Optional[T]
            state: InterpretationResultState
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
        
    @property
    def state(self) -> InterpretationState:
        return self._state
    
    @property
    def payload(self) -> Optional[T]:
        return cast(T, super().payload)
    
    @property
    def is_success(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self._state == InterpretationState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == InterpretationState.FAILURE or
                self._state == InterpretationState.TIMED_OUT
        )
    
    @property
    def nothing_to_interpret(self) -> bool:
        return (
                self.payload is None and
                self.exception is None and
                self._state == InterpretationState.NOTHING_TO_INTERPRET
        )

    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == InterpretationState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> InterpretationResult[T]:
        return cls(
            payload=payload,
            exception=None,
            state=InterpretationState.SUCCESS,
        )
    
    @classmethod
    def nothing(cls, ) -> InterpretationResult:
        return cls(
            payload=None,
            exception=None,
            state=InterpretationState.NOTHING_TO_INTERPRET,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> InterpretationResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=InterpretationState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> InterpretationResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=InterpretationState.TIMED_OUT,
        )

