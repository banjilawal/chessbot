# src/operation/collection/operator.py

"""
Module: operation.collection.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, cast

from artifcat import PromotionResult
from domain import PromotionState, Rank
from err import PromotionStateNullException
from exchange import PromotionAuthorizationRequest, PromotionAuthorizationResponder, PromotionRequest
from operation import Worker
from util import IdFactory, LoggingLevelRouter


class Promoter(Worker[PromotionResult]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces either an Insertion, Deletion, Update
            or Search Result.

    Attributes:
        authorization_responder: CollectionOperationAuthorization_Responder[T]
        
    Provides:
        -   def execute(request: CollectionRequest[T]) -> T

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
            PromotionAuthorizationRequest(
                candidate=request,
                id=IdFactory.next_id(class_name="PromotionAuthorizationRequest")
            )
        )
        if decision.is_denial:
            return PromotionResult.failure(
                PromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromoterException.MSG,
                    err_code=PromoterException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        safe = cast(PromotionRequest, decision.candidate)
        pawn_token = safe.pawn_token
        elevation = cast(Rank, cast(ABC, safe.rank_elevation))
        pawn_token.rank = elevation
        pawn_token.promotion_state = PromotionState.PROMOTED
        return PromotionResult.success(pawn_token)
        