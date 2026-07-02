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
        1.  Hold the product of an Analyzer's work.

    Attributes:
        payload: Optional[Report]
        exception: Optional[Exception]
        state: AnalysisState
        is_completed: bool
        is_aborted: bool
        is_timed_out: bool
        is_success: bool
        self.is_completed: bool
        is_failure: bool

    Provides:
        -   def completed(cls, payload: Report) -> AnalysisResult
        -   def aborted(cls, exception: Exception) -> AnalysisResult
        -   def timed_out(cls, exception: Exception) -> AnalysisResult
        -   def failure(cls, exception: Exception) -> AnalysisResult
        -   def success(payload: Report) -> AnalysisResult

    Super Class:
        Result
        
    Notes:
        An Analyzer's have three possible outcomes.
            -   An error aborts the analysis before its completed.
            -   The analysis produces a positive result.
            -   The analysis produces a negative result.
        The failure case only occurs if the analysis is completed.
        
    Recommended Factory Methods:
        -   Use completed() if the Analyzer produces a result.
        -   Use either aborted() or timed_out() if the Analyzer encounters a fatal error.
        
    Avoid Using the success() Method:
        -   For compatability with Result super class a success() implementation is provided.
        -   The success() override is a wrapper for completed() factory method.
        -   The success() method maybe be disabled in future version.
        -   The success() method does not convey an Analyzer's behavior, so it should be avoided.
        
    Using the failure() Method:
        -   The failure method is a wrapper for aborted().
        -   The failure() method overrides the super class failure method.
        -   Seeing the failure() method in analysis calls might cause confusion between the Analyzer
            aborting because of an error or producing a negative result.
        -   Despite wrapping abort(), avoid using AnalysisResult's failure method.
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
            super().is_success and
            self._state == AnalysisState.COMPLETED
        )
    
    @property
    def is_aborted(self) -> bool:
        return (
            super().is_failure and
            self.state == AnalysisState.ABORTED
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                super().is_failure and
                self.state == AnalysisState.TIMED_OUT
        )
    
    @property
    def is_success(self) -> bool:
        return self.is_completed
    
    @property
    def is_failure(self) -> bool:
        return not self.is_completed
    
    @classmethod
    def failure(cls, exception: Exception) -> AnalysisResult:
        return cls.aborted(exception)
    
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


