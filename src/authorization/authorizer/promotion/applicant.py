# src/authorization/permitter/promotion/permitter.py

"""
Module: authorization.permitter.promotion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import PromotionDecision, ValidationResult
from authorization import OperationPermitter, PromotionAuthorizationForm
from authorization.loader.promotion import PromotionAuthorizationLoader
from domain import Bishop, King, Knight, Pawn, PawnToken, Persona, Queen, Rank, RankBlueprint, Rook, Token
from err import ChessException, PawnPromoterException, PromoteInactivePawnException
from exchange import (
    PromotionRequest, RankBuildRequest, RankValidationRequest, RankValidationService, TokenValidationRequest,
    TokenValidationService
)
from fabrication import RankBuilder
from logic.promotion.promotion.exception import DoublePromotionException
from transit import PawnTokenCarrier, RankCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionApplicantReviewer:
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
    _loader: PromotionAuthorizationLoader
    _token_validation_service: TokenValidationService

    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
            token_validation_service: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
            token_validation_service: Optional[TokenValidationService
        """
        super().__init__(loader=loader or PromotionAuthorizationLoader())
        self._token_validation_service = token_validation_service or TokenValidationService()
    
    @property
    def token_validation_service(self) -> TokenValidationService:
        return self._token_validation_service
    
    @property
    def loader(self) -> PromotionAuthorizationLoader:
        return cast(PromotionAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: PromotionRequest) -> ValidationResult[PawnToken]:
        method = f"{self.__class__.__name__}.execute"
        
        loading = self.loader.execute(job)
        if loading.is_failure:
            return PromotionDecision.deny(
                request=job,
                exception=loading.exception,
            )
        request = cast(PromotionRequest, loading.payload)
        token_validation = self.token_validation_service.extract_model(
            request=TokenValidationRequest(
                item=PawnTokenCarrier(model=request.applicant),
                id=IdFactory.next_id(class_name="TokenValidationRequest")
            )
        )
        if token_validation.is_failure:
            return ValidationResult.failure(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=token_validation.exception,
                )
            )
        token = cast(Token, token_validation.payload)
        if not isinstance(token, PawnToken):
            return ValidationResult.failure(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=TypeError(
                        f"A {type(token.__class__.__name__)} cannot be promoted. "
                        f"Only a PawnToken can be elevated."
                    )
                )
            )
        applicant = cast(PawnToken, token)
        if applicant.is_promoted:
            return ValidationResult.failure(
                PawnPromoterException(
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
        position = applicant.position
        promotion_row = applicant.team.enemy_rank_row
        if position is None or position.row != promotion_row:
            return ValidationResult.failure(
                PawnPromoterException(
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
        if applicant.is_not_ready:
            return ValidationResult.failure(
                PawnPromoterException(
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
        return ValidationResult.success(applicant)