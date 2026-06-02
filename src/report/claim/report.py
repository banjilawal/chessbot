# src/report/claim/report.py

"""
Module: report.claim.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import OpeningSquare, Token
from report import Report
from report.claim.state import ClaimPermission


@dataclass
class HomeSquareClaimReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's claim on an opening square.
        
    Attributes:
        claimant: Token
        home: OpeningSquare
        
        token_has_claimed_square: bool
        square_claimed_by_other_token
        
    Provides:

    Super Class:
        Report
    """
    claimant: Token
    home: Optional[OpeningSquare]
    permissions: ClaimPermission
    
    @property
    def is_granted(self) -> bool:
        return (
                self.claimant.is_deployed and
                self.home.is_claimed and
                self.claimant.opening_square == self.home and
                self.permissions == ClaimPermission.GRANTED
        )
    
    @property
    def is_denied(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def grant_claim(cls, token: Token, home_square: OpeningSquare) -> HomeSquareClaimReport:
        return cls(
            claimant=token,
            home=home_square,
            permissions=ClaimPermission.GRANTED
        )
    
    @classmethod
    def deny_claim(cls, token: Token) -> HomeSquareClaimReport:
        return cls(
            claimant=token,
            home=None,
            permissions=ClaimPermission.DENIED
        )