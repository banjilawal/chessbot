# src/operation/promotion/worker.py

"""
Module: operation.promotion.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionResponse, PromotionResult
from domain import Bishop, King, Knight, Pawn, PromotionState, Queen, Rook
from exchange import PromotionPermissionRequest, PromotionAuthorizationResponder, PromotionRequest
from operation import Worker
from util import IdFactory, LoggingLevelRouter


class Promoter(Worker[PromotionResult]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces either an Promotion, Deletion, Update
            or Search Result.

    Attributes:
        authorization_responder: PromotionAuthorizationResponder
        
    Provides:
        -   def execute(request: PromotionRequest) -> PromotionResult

    Super Class:
        Worker
    """
    
    
    def __init__(
            self,
            authorization_responder: Optional[PromotionAuthorizationResponder] | None = None,
    ):
        """
        Args:
            authorization_responder: Optional[PromotionAuthorizationResponder]
        """
        super().__init__(
            authorization_responder=authorization_responder or PromotionAuthorizationResponder()
        )
        
    @property
    def authorization_responder(self) -> PromotionAuthorizationResponder:
        return cast(PromotionAuthorizationResponder, super().authorization_responder)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionResult:
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.authorization_responder.execute(
            PromotionPermissionRequest(
                candidate=request,
                id=IdFactory.next_id(class_name="PromotionPermissionRequest")
            )
        )
        if decision.request_is_denied:
            return PromotionResult.failure(
                ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromoterException.MSG,
                    err_code=PromoterException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        safe = cast(PromotionRequest, decision.request)
        applicant = safe.applicant
        rank = safe.elevatable_to_rank
        promotion = Pawn()
        
        if isinstance(rank, Bishop):
            promotion = Bishop()
        if isinstance(rank, Knight):
            promotion = Knight()
        if isinstance(rank, Queen):
            promotion = Queen()
        if isinstance(rank, Rook):
            promotion = Rook()
        
        if isinstance(promotion, (Pawn, King)):
            return PromotionResult.failure(
                PromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromoterException.MSG,
                    err_code=PromoterException.ERR_CODE,
                    ex=PromotionRouteException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromotionRouteException.MSG,
                        err_code=NoPromotionRouteException.ERR_CODE,
                    ),
                )
            )
        applicant.rank = promotion
        applicant.promotion_state = PromotionState.PROMOTED
        return PromotionResult.success(applicant)
        