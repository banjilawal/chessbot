# src/report/claim/report.py

"""
Module: report.claim.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model import OpeningSquare, Token


@dataclass
class HomeSquareClaimReport:
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's claim on an opening square.
        
    Attributes:
        token: Token
        square: OpeningSquare
        
        token_has_claimed_square: bool
        square_claimed_by_other_token
        
    Provides:

    Super Class:
        Report
    """
    token: Token
    square: OpeningSquare
    
    @property
    def token_has_claimed_square(self) -> bool:
        return (
                self.token.is_deployed and
                self.square.is_claimed and
                self.token == self.square.occupant
        )
    
    @property
    def square_claimed_by_other_token(self) -> bool:
        return self.square.is_claimed and self.token != self.square.occupant