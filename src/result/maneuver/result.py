# src/result/maneuver/result.py

"""
Module: result.maneuver.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from event import Event
from result import EventState, Result


@dataclass(frozen=True)
class EventResult(Result[Event]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains outcome of a maneuver transaction.

    Attributes:
        exception: Optional[Exception]
        state: ManeuverState
        payload: Optional[ManeuverEvent]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(r) -> ManeuverResult[ManeuverEvent]
        -   def failure(exception: Exception) -> ManeuverResult[ManeuverEvent]
        -   def timed_out(exception: Exception) -> ManeuverResult[ManeuverEvent]
        
    Super Class:
        Result
    """
    state: EventState
    payload: Optional[Event] = None
    exception: Optional[Exception] = None


    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state == EventState.FAILURE or
                self.state == EventState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state == EventState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: Event) -> EventResult[Event]:
        return cls(
            payload=payload,
            exception=None,
            state=EventState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> EventResult[Event]:
        return cls(
            payload=None,
            exception=exception,
            state=EventState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> EventResult[Event]:
        return cls(
            payload=None,
            exception=exception,
            state=EventState.TIMED_OUT,
        )
