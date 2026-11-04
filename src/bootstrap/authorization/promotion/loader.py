# src/bootstrap/authorization/promotion/loader.py

"""
Module: bootstrap.authorization.promotion.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import PromotionDecision
from bootstrap import AuthorizationLoader
from domain import Rank, PawnToken, Rank, Token
from err import PromotionRequestNullException
from exchange import (
    PromotionPermissionRequest, PromotionRequest, RankValidationRequest, RankValidationService,
    TokenValidationRequest, TokenValidationService
)
from transit import RankCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionAuthorizationLoader(
    AuthorizationLoader[PromotionPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Run basic type and validation checks on items entering the
            permitting process.

    Attributes:

    Provides:
        -   def execute(candidate: Any) -> PromotionDecision

    Super Class:
        AuthorizationLoader
    """
    
    _rank_validation_service: RankValidationService
    _token_validation_service: TokenValidationService

    
    def __init__(
            self,
            rank_validation_service: Optional[RankValidationService] | None = None,
            token_validation_service: Optional[TokenValidationService] | None = None
    ):
        """
        Args:
            rank_validation_service: Optional[RankValidationService]
            token_validation_service: Optional[TokenValidationService]
        """
        super().__init__()
        self._rank_validation_service = (
                rank_validation_service or RankValidationService()
        )
        self._token_validation_service = (
                token_validation_service or TokenValidationService()
        )
        
    @property
    def rank_validation_service(self) -> RankValidationService:
        return self._rank_validation_service
    
    @property
    def token_validation_service(self) -> TokenValidationService:
        return self._token_validation_service
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> PromotionDecision:
        """
        Checks if the request is null or the wrong type

        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   not a PromotionPermissionRequest.
            2.  Otherwise, send an approval.
        Args:
            candidate: PromotionPermissionRequest
        Returns:
           PromotionDecision
        Raises:
            PromotionAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader cannot get primed
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=PromotionPermissionRequest,
            null_exception=PromotionPermissionRequestNullException(),
        )
        if priming.is_failure:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                   cls_mthd=method,
                   cls_name=self.__class__.__name__,
                   msg=PromotionAuthorizationLoaderException.MSG,
                   err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                   ex=priming.exception,
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(PromotionPermissionRequest, priming.payload)

        # Handle the case that the permissio_form does not have an id.
        form_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if form_id_validation.is_failure:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=form_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant,
            target_model=PromotionRequest,
            null_exception=PromotionRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Cast the applicant to validate its contents. ---#
        applicant = cast(PromotionRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_APPLICANT_ID_ATTRIBUTE. ---#
        applicant_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if applicant_id_validation.is_failure:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_id_validation.exception,
                )
            )
        # --- PROCESS_THE_PROMOTION_CANDIDATE_ATTRIBUTE. ---#
        token_validation = self._token_validation_service.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=applicant.token),
                id=IdFactory.next_id("TokenValidationRequest")
            )
        )
        # Handle the case that the applicant is not Token.
        if token_validation.is_failure:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=token_validation.exception,
                )
            )
        # Handle the case that the promotion_candidate token is not a PawnToken
        if not isinstance(token_validation.payload, PawnToken):
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=TypeError(
                        f"Expected PawnToken got "
                        f"{type(token_validation.payload).__name__} instead."
                    ),
                )
            )
        # --- PROCESS_THE_PROMOTION_RANK_ATTRIBUTE. ---#
        rank_validation = self._rank_validation_service.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=applicant.elevatable_to_rank),
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        # Handle the case that the promotion rank is not safe.
        if rank_validation.is_failure:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=rank_validation.exception
                )
            )
        # Handle the case that the rank is not an Elevatable
        if not isinstance(rank_validation.payload, Rank):
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=rank_validation.exception
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        pawn_token = cast(PawnToken, token_validation.payload)
        transaction_id = cast(int, applicant_id_validation.payload)
        permission_id = cast(int, form_id_validation.payload)
        elevatable = cast(Rank, cast(object, rank_validation.payload))
        
        # --- Prepare a transaction approval. ---#
        approved_applicant = PromotionRequest(
            id=transaction_id,
            token=pawn_token,
            promotion_level=elevatable,
        )
        permission_request = PromotionPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )