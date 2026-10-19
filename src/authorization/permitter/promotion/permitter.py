# src/authorization/permitter/promotion/permitter.py

"""
Module: authorization.permitter.promotion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import PromotionDecision
from authorization import OperationPermitter, PromotionAuthorizationForm
from authorization.loader.promotion import PromotionAuthorizationLoader
from domain import PawnToken, Rank, Token
from err import ChessException, PawnPromoterException, PromoteInactivePawnException
from exchange import (
    PromotionRequest, RankValidationRequest, RankValidationService, TokenValidationRequest,
    TokenValidationService
)
from logic.promotion.promotion.exception import DoublePromotionException
from transit import PawnTokenCarrier, RankCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionPermitter(OperationPermitter[PromotionDecision]):
    """
    Role:
        -   Permission Authorization
        -   Consistency and Integrity Management

    Responsibilities:
        1.  Check if a PawnToken satisfies promotion requirements.

    Attributes:
        loader: PromotionAuthorizationLoader
        rank_validation_service: RankValidationService
        token_validation_service: TokenValidationServic

    Provides:
        -  def process(form: PromotionAuthorizationForm) -> PromotionDecision

    Super Class:
        OperationPermitter
    """
    _rank_validation_service: RankValidationService
    _token_validation_service: TokenValidationService
    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
            rank_validation_service: Optional[RankValidationService] | None = None,
            token_validation_service: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
            rank_validation_service: Optional[RankValidationService]
            token_validation_service: Optional[TokenValidationService
        """
        super().__init__(loader=loader or PromotionAuthorizationLoader())
        self._rank_validation_service = rank_validation_service or RankValidationService()
        self._token_validation_service = token_validation_service or TokenValidationService()
    
    @property
    def rank_validation_service(self) -> RankValidationService:
        return self._rank_validation_service
    
    @property
    def token_validation_service(self) -> TokenValidationService:
        return self._token_validation_service
    
    @property
    def loader(self) -> PromotionAuthorizationLoader:
        return cast(PromotionAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: PromotionRequest) -> PromotionDecision:
        method = f"{self.__class__.__name__}.execute"
        
        loading = self.loader.execute(job)
        if loading.is_failure:
            return PromotionDecision.deny(
                request=job,
                exception=loading.exception,
            )
        request = cast(PromotionRequest, loading.payload)
        
        id_validation = self.loader.identity_service.validate_id(request.id)
        if id_validation.is_failure:
            return PromotionDecision.deny(
                request=request,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        token_validation = self.token_validation_service.extract_model(
            request=TokenValidationRequest(
                item=PawnTokenCarrier(model=request.applicant),
                id=IdFactory.next_id(class_name="TokenValidationRequest")
            )
        )
        if token_validation.is_failure:
            return PromotionDecision.deny(
                request=request,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=token_validation.exception,
                )
            )
        applicant = cast(Token, token_validation.payload)
        if not isinstance(applicant, PawnToken):
            return PromotionDecision.deny(
                request=request,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=TypeError(f"Cannot promote a {type(applicant.__class__.__name__)}.")
                )
            )
        pawn = cast(PawnToken, applicant)
        if pawn.is_promoted:
            return PromotionDecision.deny(
                request=request,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    ex=DoublePromotionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DoublePromotionException.MSG,
                        err_code=DoublePromotionException.ERR_CODE,
                    )
                )
            )
        promotion_row = pawn.team.enemy_rank_row
        if pawn.position.row != promotion_row:
            return PromotionDecision.deny(
                request=request,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    ex=PromotionRowException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromotionRowException.MSG,
                        err_code=PromotionRowException.ERR_CODE,
                    )
                )
            )
        if pawn.is_not_ready:
            return PromotionDecision.deny(
                request=request,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    ex=PromoteInactivePawnException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromoteInactivePawnException.MSG,
                        err_code=PromoteInactivePawnException.ERR_CODE,
                    )
                )
            )
        rank_validation = self.rank_validation_service.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=request.rank_elevation),
                id=IdFactory.next_id(class_name="RankValidationRequest"),
            )
        )
        rank = cast(Rank, rank_validation.payload)
        if rank not in PawnToken.PROMOTION_RANKS:
            return PromotionDecision.deny(
                request=request,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    ex=PromoteInactivePawnException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromoteInactivePawnException.MSG,
                        err_code=PromoteInactivePawnException.ERR_CODE,
                    )
                )
            )
        approved_request = PromotionRequest(
            id=cast(int, id_validation.payload),
            applicant=pawn,
            elevated_rank=rank,
        )
        return PromotionDecision.grant(
            request=approved_request
        )
        