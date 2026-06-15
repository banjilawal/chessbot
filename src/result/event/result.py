# src/result/event/result.py

"""
Module: result.event.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from event import Event
from result import EventState, Result



class EventResult(Result[Event]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains outcome of a event transaction.

    Attributes:
        exception: Optional[Exception]
        state: EventState
        payload: Optional[EventEvent]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(r) -> EventResult[EventEvent]
        -   def failure(exception: Exception) -> EventResult[EventEvent]
        -   def timed_out(exception: Exception) -> EventResult[EventEvent]
        
    Super Class:
        Result
    """
    _state: EventState
    
    def __init__(
            self,
            state: EventState,
            payload: Optional[Event] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: SearchState
            payload: Optional[Event]
            exception: Optional[Exception]
        """
        super().__init__(payload=payload, exception=exception)
        """INTERNAL: Use Search methods instead of direct constructor."""
        self._state = state


    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == EventState.FAILURE or
                self._state == EventState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == EventState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: Event) -> EventResult:
        return cls(
            payload=payload,
            exception=None,
            state=EventState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> EventResult:
        return cls(
            payload=None,
            exception=exception,
            state=EventState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> EventResult:
        return cls(
            payload=None,
            exception=exception,
            state=EventState.TIMED_OUT,
        )
