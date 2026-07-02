# src/report/freedom/report.py

"""
Module: report.freedom.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import CombatantToken, KingToken, Token
from report import ReadinessState, Report


@dataclass
class TokenReadinessReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents the results of testing if a Token can be used in the game.
        
    Attributes:
        token: Token
        state: FreedomState
        
        is_free: bool
        is_not_free: bool
        is_captured: bool
        is_checkmated: bool
        is_not_deployed: bool
        
    Provides:
        -   def free(token: Token) -> TokenFreedomReport:
        -   def not_deployed(token: Token) -> TokenFreedomReport:
        -   def captured(token: CombatantToken) -> TokenFreedomReport:
        -   def checkmated(token: KingToken) -> TokenFreedomReport:

    Super Class:
        Report
    """
    token: Token
    state: ReadinessState
    
    @property
    def is_ready(self) -> bool:
        return self.state == ReadinessState.READY
    
    @property
    def token_is_not_ready(self) -> bool:
        return self.state != ReadinessState.READY
    
    @property
    def is_captured(self) -> bool:
        return (
                isinstance(self.token, CombatantToken) and
                self.state == ReadinessState.CAPTURED
        )
    
    @property
    def is_disabled(self) -> bool:
        return (
                self.state == ReadinessState.DISABLED and
                self.token.is_disabled
        )
    
    @property
    def is_not_deployed(self) -> bool:
        return self.state == ReadinessState.NOT_DEPLOYED
    
    @property
    def is_deployed(self) -> bool:
        return (
                self.state != ReadinessState.NOT_DEPLOYED and
                self.token.is_not_deployed
        )

    @property
    def is_checkmated(self) -> bool:
        return (
                isinstance(self.token, KingToken) and
                self.state == ReadinessState.CHECKMATED
        )
    
    @classmethod
    def ready(cls, token: Token) -> TokenReadinessReport:
        return cls(token=token, state=ReadinessState.READY)
    
    @classmethod
    def not_deployed(cls, token: Token) -> TokenReadinessReport:
        return cls(token=token, state=ReadinessState.NOT_DEPLOYED)
    
    @classmethod
    def disabled(cls, token: Token) -> TokenReadinessReport:
        return cls(token=token, state=ReadinessState.DISABLED)
    
    @classmethod
    def captured(cls, token: CombatantToken) -> TokenReadinessReport:
        return cls(token=token, state=ReadinessState.CAPTURED)
    
    @classmethod
    def checkmated(cls, token: KingToken) -> TokenReadinessReport:
        return cls(token=token, state=ReadinessState.CHECKMATED)