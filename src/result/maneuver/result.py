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

from event import ManeuverEvent
from result import ManeuverState, Result


@dataclass(frozen=True)
class ManeuverResult(Result[ManeuverEvent]):
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
    state: ManeuverState
    exception: Optional[Exception] = None
    payload: Optional[ManeuverEvent] = None

    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state == ManeuverState.FAILURE or
                self.state == ManeuverState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state == ManeuverState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: ManeuverEvent) -> ManeuverResult[ManeuverEvent]:
        return cls(
            payload=payload,
            exception=None,
            state=ManeuverState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ManeuverResult[ManeuverEvent]:
        return cls(
            payload=None,
            exception=exception,
            state=ManeuverState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ManeuverResult[ManeuverEvent]:
        return cls(
            payload=None,
            exception=exception,
            state=ManeuverState.TIMED_OUT,
        )
