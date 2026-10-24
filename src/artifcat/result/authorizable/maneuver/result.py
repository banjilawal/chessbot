# src/artifact/result/authorizable/maneuver/result.py

"""
Module: artfifact.result.authorizable.maneuver.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Result, ResultState
from domain import Maneuver


class ManeuverResult(Result[Maneuver]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains details of a Maneuver transaction.


    Attributes:
        state: resultState
        payload: Optional[Maneuver]
        exception: Optional[Exception]
        
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: Maneuver) -> ManeuverResult
        -   def failure(exception: Exception) -> ManeuverResult
        -   def timed_out(cls, exception: Exception) -> ManeuverResult:

    Super Class:
        Result
    """
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[Maneuver] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[Maneuver]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception
        )
    
    @property
    def payload(self) -> Optional[Maneuver]:
        return cast(Maneuver, super().payload)
    
    @property
    def is_success(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self.state == ResultState.SUCCESS and
            isinstance(self.payload, Maneuver)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.success
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ResultState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: Maneuver) -> ManeuverResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ManeuverResult:
        return cls(
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ManeuverResult:
        return cls(
            exception=exception,
            state=ResultState.TIMED_OUT,
        )