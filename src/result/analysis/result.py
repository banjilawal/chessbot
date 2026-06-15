# src/result/analysis/result.py

"""
Module: result.analysis.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from report import Report
from result import AnalysisState, Result


class AnalysisResult(Result[Report]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of a analysis.

    Attributes:
        exception: Optional[Exception]
        state: validationState
        payload: Optional[R]
        is_timed_out: bool
        is_success: bool
        is_failure: bool
        is_nothing_to_analysis: bool

    Provides:
        -   def success(payload: T) -> AnalysisResu[R]
        -   def failure(exception: Exception) -> AnalysisResu[R]
        -   def timed_out(exception: Exception) -> AnalysisResult[R]
        -   def nothing_to_analysis() -> AnalysisResult[R]

    Super Class:
        Result
    """
    _state = AnalysisState
    
    def __init__(
            self,
            state: AnalysisState,
            payload: Optional[Report] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            payload: Optional[R]
            state: AnalysisResultState
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
        
    @property
    def state(self) -> AnalysisState:
        return self._state
    
    @property
    def is_completed(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self._state == AnalysisState.COMPLETED
        )
    
    @property
    def is_aborted(self) -> bool:
        return not self.is_completed
    
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == AnalysisState.TIMED_OUT
        )
    
    @classmethod
    def completed(cls, payload: Report) -> AnalysisResult:
        return cls(
            payload=payload,
            exception=None,
            state=AnalysisState.COMPLETED,
        )
    
    @classmethod
    def aborted(cls, exception: Exception) -> AnalysisResult:
        return cls(
            payload=None,
            exception=exception,
            state=AnalysisState.ABORTED,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> AnalysisResult:
        return cls(
            payload=None,
            exception=exception,
            state=AnalysisState.TIMED_OUT,
        )


