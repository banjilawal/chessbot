# src/report/freedom/report.py

"""
Module: report.freedom.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from model import CombatantToken, KingToken, Token
from report import FreedomState

@dataclass
class TokenFreedomReport:
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
    state: FreedomState
    
    @property
    def token_is_free(self) -> bool:
        return self.state == FreedomState.FREE
    
    @property
    def token_is_not_free(self) -> bool:
        return self.state != FreedomState.FREE
    
    @property
    def token_is_captured(self) -> bool:
        return isinstance(self.token, CombatantToken) and self.state == FreedomState.CAPTURED
    
    @property
    def token_is_disabled(self) -> bool:
        return self.state == FreedomState.DISABLED and self.token.is_disabled
    
    @property
    def token_is_deployed(self) -> bool:
        return self.state != FreedomState.NOT_DEPLOYED and self.token.is_not_deployed
    
    @property
    def token_is_not_deployed(self) -> bool:
        return self.state == FreedomState.NOT_DEPLOYED
    
    @property
    def is_checkmated(self) -> bool:
        return isinstance(self.token, KingToken) and self.state == FreedomState.CHECKMATED
    
    @classmethod
    def free(cls, token: Token) -> TokenFreedomReport:
        return cls(token=token, state=FreedomState.FREE)
    
    @classmethod
    def not_deployed(cls, token: Token) -> TokenFreedomReport:
        return cls(token=token, state=FreedomState.NOT_DEPLOYED)
    
    @classmethod
    def disabled(cls, token: Token) -> TokenFreedomReport:
        return cls(token=token, state=FreedomState.DISABLED)
    
    @classmethod
    def captured(cls, token: CombatantToken) -> TokenFreedomReport:
        return cls(token=token, state=FreedomState.CAPTURED)
    
    @classmethod
    def checkmated(cls, token: KingToken) -> TokenFreedomReport:
        return cls(token=token, state=FreedomState.CHECKMATED)