# src/operation/promotion/worker.py

"""
Module: operation.promotion.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionResult
from domain import Bishop, King, Knight, Pawn, PromotionState, Queen, Rook
from exchange import PromotionPermissionRequest, PromotionRequest
from operation import Worker
from transit import PromotionPermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class Promoter(Worker[PromotionRequest, PromotionResult]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Execute a PromotionRequest.

    Attributes:
        permitter: PromotionPermissionDispatcher
        
    Provides:
        -   def execute(request: PromotionRequest) -> PromotionResult

    Super Class:
        Worker
    """
    
    
    def __init__(
            self,
            permitter: Optional[PromotionPermissionDispatcher] | None = None,
    ):
        """
        Args:
            permitter: Optional[PromotionPermissionDispatcher]
        """
        super().__init__(
            permitter=permitter or PromotionPermissionDispatcher()
        )
        
    @property
    def permitter(self) -> PromotionPermissionDispatcher:
        return cast(PromotionPermissionDispatcher, super().permitter)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionResult:
        method = f"{self.__class__.__name__}.execute"
        
        # --- Get work authorization. ---#
        decision = self.permitter.execute(
            candidate=PromotionPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="PromotionPermissionRequest")
            )
        )
        # Handle the case that the request is not authorized.
        if decision.request_is_denied:
            return PromotionResult.failure(
                PromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromoterException.MSG,
                    err_code=PromoterException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = decision.permission_request
        transaction_request = decision.transaction_request
        
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return PromotionResult.failure(
                exception=PromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromoterException.MSG,
                    err_code=PromoterException.ERR_CODE,
                    ex=PromotionPermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return PromotionResult.failure(
                exception=PromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromoterException.MSG,
                    err_code=PromoterException.ERR_CODE,
                    ex=PromotionRequestNullException()
                )
            )
        # --- Extract the transaction participants. ---#
        pawn_token = transaction_request.token
        rank = transaction_request.elevatable_to_rank
        promotion = Pawn()
        
        # --- Perform transaction and state management work. ---#
        if isinstance(rank, Bishop):
            promotion = Bishop()
        if isinstance(rank, Knight):
            promotion = Knight()
        if isinstance(rank, Queen):
            promotion = Queen()
        if isinstance(rank, Rook):
            promotion = Rook()
        # Handle the case that the rank is not covered by the process.
        if promotion is None or isinstance(promotion, (Pawn, King)):
            return PromotionResult.failure(
                PromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromoterException.MSG,
                    err_code=PromoterException.ERR_CODE,
                    ex=PromotionRouteCoverageException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromotionRouteCoverageException.MSG,
                        err_code=PromotionRouteCoverageException.ERR_CODE,
                    ),
                )
            )
        pawn_token.rank = promotion
        pawn_token.promotion_state = PromotionState.PROMOTED
        # --- Forward the work product to the client. ---#
        return PromotionResult.success(pawn_token)
        