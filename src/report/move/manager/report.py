# src/report/move/manager/report.py

"""
Module: report.move.manager.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from report import Report
from model import PawnToken, MoveState
from report.move.manager.state import MoveDecision


@dataclass
class MoveApprovalManagerReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's move on an opening square.
        
    Attributes:
        decision: MoveDecision
        move_row: Optional[int]
        requestor: Optional[PawnToken]
        execption: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def approve_move(cls, pawn: PawnToken) -> MoveApprovalManagerReport:
        -   def deny_move(cls, exception: Exception) -> MoveApprovalManagerReport:
    Super Class:
        Report
    """
    decision: MoveDecision
    requestor: Optional[PawnToken] = None
    move_row: Optional[int] = None
    exception: Optional[Exception] = None
    
    
    @property
    def is_granted(self) -> bool:
        return (
                self.requestor.is_active and
                self.exception is None and
                self.decision == MoveDecision.ATTACK_ENEMY_SQUARE and
                self.requestor.move_state == MoveState.NOT_PROMOTED and
                self.requestor.current_position.row == self.move_row
        )
    
    @property
    def is_denied(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def approve_move(cls, pawn: PawnToken) -> MoveApprovalManagerReport:
        return cls(
            requestor=pawn,
            decision=MoveDecision.ATTACK_ENEMY_SQUARE,
            move_row=pawn.team.schema.enemy_schema.rank_row,
            exception=None,
        )
    
    @classmethod
    def deny_move(cls, exception: Exception) -> MoveApprovalManagerReport:
        return cls(
            decision=MoveDecision.OCCUPY_EMPTY_SQUARE,
            move_row=None,
            requestor=None,
            exception=exception,
        )
    