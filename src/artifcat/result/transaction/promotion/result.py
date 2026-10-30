# src/artifact/result/transaction/promotion/result.py

"""
Module: artfifact.result.transaction.promotion.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ResultState
from domain import PawnToken, Rank


class PromotionResult(TransactionResult[PawnToken]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains the outcome of an Promotion transaction.


    Attributes:
        state: resultState
        payload: Optional[PawnToken]
        exception: Optional[Exception]

    Provides:
        -   def success(payload: PawnToken) -> PromotionResult

    Super Class:
        Result
    """
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[PawnToken] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[PawnToken]
            exception: Optional[Exception]
        """
        super().__init__(state=state, payload=payload, exception=exception)
    
    @property
    def payload(self) -> Optional[PawnToken]:
        return cast(PawnToken, super().authorization_applicant)
    
    @property
    def promotion(self) -> Optional[Rank]:
        pawn_token = self.payload
        if pawn_token is None:
            return None
        return pawn_token.rank
        
    
    @property
    def is_success(self) -> bool:
        return super().is_success and isinstance(self.payload, PawnToken)
    
    @property
    def is_failure(self) -> bool:
        return not self.success
    
    @classmethod
    def success(cls, payload: PawnToken) -> PromotionResult:
        return cls(payload=payload, state=ResultState.SUCCESS)