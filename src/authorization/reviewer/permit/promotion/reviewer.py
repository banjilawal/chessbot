# src/authorization/reviewer/role/promotion/reviewer.py

"""
Module: authorization.reviewer.role.promotion.reviewer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from authorization import RoleReviewer, PromotionAuthorizationLoader
from domain import Bishop, King, Knight, Pawn, PawnRank, ChessException, PawnToken, Persona, Queen, Rank, Rook
from err import ChessException, PromoteInactivePawnException
from exchange import PromotionRequest, RankValidationRequest, RankValidationService
from logic.promotion.promotion.exception import DoublePromotionException
from transit import PawnRankCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionChessExceptionReviewer(RoleReviewer[ChessException]):
    """
    Role:
        -   Permission Authorization
        -   Consistency and Integrity Management

    Responsibilities:
        1.  Check if a PawnRank satisfies promotion requirements.

    Attributes:
        loader: PromotionAuthorizationLoader
        rank_validation_service: RankValidationService

    Provides:
        -  def process(form: PromotionAuthorizationForm) -> PromotionDecision

    Super Class:
        RoleReviewer
    """
    _loader: PromotionAuthorizationLoader
    _rank_validation_service: RankValidationService

    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
            rank_validation_service: Optional[RankValidationService] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
            rank_validation_service: Optional[RankValidationService
        """
        super().__init__()
        self._loader = loader or PromotionAuthorizationLoader()
        self._rank_validation_service = rank_validation_service or RankValidationService()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, application: PromotionRequest) -> ValidationResult[PawnRank]:
        method = f"{self.__class__.__name__}.execute"
        
        loading = self._loader.execute(application)
        if loading.is_failure:
            return ValidationResult.failure(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        request = cast(PromotionRequest, loading.payload)
        rank_validation = self._rank_validation_service.extract_model(
            request=RankValidationRequest(
                item=PawnRankCarrier(model=request.rank_elevation),
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        if rank_validation.is_failure:
            return ValidationResult.failure(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=rank_validation.exception,
                )
            )
        elevated_rank = Pawn()
        persona = cast(Rank, rank_validation.payload).persona

        if persona == Persona.BISHOP:
            elevated_rank = Bishop()
        if persona == Persona.KING:
            elevated_rank = King()
        if persona == Persona.KNIGHT:
            elevated_rank = Knight()
        if persona == Persona.PAWN:
            elevated_rank = Pawn()
        if persona == Persona.QUEEN:
            elevated_rank = Queen()
        if persona == Persona.ROOK:
            elevated_rank = Rook()
        if elevated_rank not in PawnToken.PROMOTION_RANKS:
            return ValidationResult.failure(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=PromotionRankBoundsException(),
                )
            )
        return ValidationResult.success(elevated_rank)