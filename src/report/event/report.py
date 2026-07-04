# src/report/event/report.py

"""
Module: report.event.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import HomeSquare, Token
from report import Report
from report.event.state import EventPermission


@dataclass
class EventTransitionReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's event on an opening square.
        
    Attributes:
        eventant: Token
        home_square: OpeningSquare
        
        token_has_evented_square: bool
        square_evented_by_other_token
        
    Provides:

    Super Class:
        Report
    """
    event: Event
    transition: Optional[EventTransition] = None
    exception: Optional[Exception] = None
    
    @property
    def is_granted(self) -> bool:
        return (
                self.eventant.is_deployed and
                self.home_square.is_evented and
                self.exception is None and
                self.eventant.home_square == self.home_square and
                self.permissions == EventPermission.GRANTED
        )
    
    @property
    def is_denied(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def grant_event(cls, token: Token, home_square: HomeSquare) -> EventTransitionReport:
        return cls(
            eventant=token,
            home_square=home_square,
            permissions=EventPermission.GRANTED,
            exception=None
        )
    
    @classmethod
    def deny_event(cls, token: Token, exception: Exception,) -> EventTransitionReport:
        return cls(
            eventant=token,
            home_square=None,
            permissions=EventPermission.DENIED,
            exception=exception,
        )