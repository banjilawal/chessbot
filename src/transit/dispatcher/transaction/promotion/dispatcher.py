# src/transit/dispatcher/promotion/dispatcher.py

"""
Module: transit.dispatcher.promotion.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionResult
from domain import PawnToken
from operation import Promoter
from request import PromotionRequest
from transit import TransactionDispatcher
from util import LoggingLevelRouter

class PromotionDispatcher(TransactionDispatcher[PromotionResult]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute PromotionRequests among workers then send the result to the correct client

    Attributes:
        worker: Promoter

    Provides:
        -   def  execute(self, request: PromotionRequest) -> PromotionResult

    Super Class:
        TransactionDispatcher
    """
    
    
    def __init__(self, worker: Optional[Promoter] | None = None):
        """
        Args:
            worker: Optional[Promoter]
        """
        super().__init__(worker=worker or Promoter())
        
    @property
    def worker(self) -> Promoter:
        return cast(Promoter, super().worker)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionResult:
        """
        Distribute PromotionRequests among workers then forward the results.
        
        Action:
            1.  Send an exception chain in the Result if the request cannot be satisfied.
            2.  Otherwise, send the success result.
        Args:
            request: PromotionRequest
        Returns:
            PromotionResult
        Raises:
            PromotionDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send an exception chain in the result.
            return PromotionResult.failure(
                PromotionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionDispatcherException.MSG,
                    err_code=PromotionDispatcherException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        pawn = cast(PawnToken, result.payload)
        return PromotionResult.success(pawn)
        