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
from domain import Elevatable, PawnToken, Rank, Token
from domain.interface.actionable import elevatable
from err import PromotionRequestNullException
from exchange import (
    PromotionPermissionRequest, PromotionRequest, RankValidationRequest, RankValidationService, TokenValidationRequest,
    TokenValidationService
)
from transit import RankCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionAuthorizationLoader(
    AuthorizationLoader[PromotionPermissionRequest]
):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure only not-null PermissionRequest is processed.

    Attributes:

    Provides:
        -   def execute(request: PromotionPermissionRequest) -> PromotionDecision

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
        # --- Get the permission_request for type checking the applicant. ---#
        permission_form = cast(PromotionPermissionRequest, priming.payload)
        
        # Handle the case that the permissio_form does not have an id.
        permission_form_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_form_id_validation.is_failure:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=permission_form_id_validation.exception,
                )
            )
        permission_form_id = cast(int, permission_form_id_validation.payload)
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
        # --- Get the permission_request for type checking the applicant. ---#
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
        applicant_id = cast(int, applicant_id_validation.payload)
        # --- PROCESS_THE_PROMOTION_CANDIDATE_ATTRIBUTE. ---#
        token_validation = self._token_validation_service.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=applicant.promotion_candidate),
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
        token = cast(Token, token_validation.payload)
        # Handle the case that the promotion_candidate token is not a PawnToken
        if not isinstance(token, PawnToken):
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationLoaderException.MSG,
                    err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                    ex=TypeError(
                        f"Expected PawnToken got {type(token).__name__} instead."
                    ),
                )
            )
        pawn_token = cast(PawnToken, token)
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
        rank = cast(Rank, rank_validation.payload)
        elevatable = cast(Elevatable, rank)
        # Handle the case that the rank is not an Elevatable
        if not isinstance(rank, Elevatable):
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
        # --- Prepare an approval from the completed chain. ---#
        approved_applicant = PromotionRequest(
            id=applicant_id,
            applicant=pawn_token,
            elevatable=elevatable,
        )
        approval = PromotionPermissionRequest(
            id=permission_form_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(PathPrimeExtract, bootstrap.payload)
        carrier = extract.reference
        fingerprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=PathCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathCarrierEmptyException.MSG,
                        err_code=PathCarrierEmptyException.ERR_CODE,
                    ),
                )
            )

        label = fingerprint.label
        if label is not None:
            label_validation = self.loader.toolkit.number_validator.execute(label)
            # Handle the case that the endpoints are flagged.
            if label_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PathValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathValidatorException.MSG,
                        err_code=PathValidatorException.ERR_CODE,
                        ex=label_validation.exception,
                    )
                )
            label = cast(int, label_validation.payload)
        # --- PROCESS_THE_ENDPOINTS_ATTRIBUTE. ---#
        endpoints_validation = self.loader.toolkit.dependency.square_register.extract_model(
            request=SquareRegisterValidationRequest(
                item=SquareRegisterCarrier(model=fingerprint.endpoints),
                id=IdFactory.next_id(class_name="SquareRegisterValidationRequest"),
            )
        )
        # Handle the case that the endpoints are flagged.
        if endpoints_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=endpoints_validation.exception,
                )
            )
