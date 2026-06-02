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

from model import OpeningSquare, PawnToken, PromotionState, Token
from report import Report
from report.promote.state import PromotionPermission


@dataclass
class PromotionReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's claim on an opening square.
        
    Attributes:
        claimant: Token
        home_square: OpeningSquare
        
        token_has_claimed_square: bool
        square_claimed_by_other_token
        
    Provides:

    Super Class:
        Report
    """
    pawn: PawnToken
    promotion_row: Optional[int]
    permission: PromotionPermission
    
    
    @property
    def can_promote(self) -> bool:
        return (
            self.pawn.is_active and
            self.permission == PromotionPermission.GRANTED and
            self.pawn.promotion_state == PromotionState.NOT_PROMOTED and
            self.pawn.current_position.row == self.promotion_row
        )
    
    @property
    def cannot_promote(self) -> bool:
        return not self.can_promote
    
    @classmethod
    def grant_promotion(cls, pawn: PawnToken) -> PromotionReport:
        return cls(
            pawn=pawn,
            permission=PromotionPermission.GRANTED,
            promotion_row=pawn.team.schema.enemy_schema.rank_row,
        )
    
    @classmethod
    def deny_promotion(cls, pawn: PawnToken) -> PromotionReport:
        return cls(
            pawn=pawn,
            permission=PromotionPermission.DENIED,
            promotion_row=None,
        )
    