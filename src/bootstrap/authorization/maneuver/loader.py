# src/bootstrap/authorization/maneuver/loader.py

"""
Module: bootstrap.authorization.maneuver.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ManeuverDecision
from bootstrap import AuthorizationLoader
from domain import Path, Token
from err import (
    ManeuverAuthorizationLoaderException, ManeuverPermissionRequestNullException,
    ManeuverRequestNullException
)

from exchange import (
    ManeuverPermissionRequest, ManeuverRequest, PathValidationRequest,
    PathValidationService, TokenValidationRequest, TokenValidationService
)
from transit import PathCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class ManeuverAuthorizationLoader(
    AuthorizationLoader[ManeuverPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Run basic type and validation checks on items entering the maneuver 
            permitting process.

    Attributes:
        path_validation_service: PathValidationService
        token_validation_service: TokenValidationService

    Super Class:
        AuthorizationLoader
    """
    
    _path_validation_service: PathValidationService
    _token_validation_service: TokenValidationService
    
    def __init__(
            self,
            path_validation_service: Optional[PathValidationService] | None = None,
            token_validation_service: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            path_validation_service: Optional[PathValidationService]
            token_validation_service: Optional[TokenValidationService]
        """
        super().__init__()
        self._path_validation_service = path_validation_service or PathValidationService()
        self._token_validation_service = token_validation_service or TokenValidationService()
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ManeuverDecision:
        """
        Checks if the request is null or the wrong type

        Action:
            1.  Send an exception chain in the Decision denial if any of the following
                occurred
                    -   The candidate is not a ManeuverPermissionRequest
                    -   The PermissionRequest does not contain a ManeuverRequest.
                    -   Either the token or path in the request cannot be validated.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           ManeuverDecision
        Raises:
            ManeuverAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=ManeuverPermissionRequest,
            null_exception=ManeuverPermissionRequestNullException(),
        )
        # Send an exception chain in the denial.
        if priming.is_failure:
            return ManeuverDecision.denial(
                exception=ManeuverAuthorizationLoaderException(
                   cls_mthd=method,
                   cls_name=self.__class__.__name__,
                   msg=ManeuverAuthorizationLoaderException.MSG,
                   err_code=ManeuverAuthorizationLoaderException.ERR_CODE,
                   ex=priming.exception,
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(
            ManeuverPermissionRequest, 
            priming.payload,
        )
        # Handle the case that the permission_form does not have an id.
        form_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if form_id_validation.is_failure:
            # Send an exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizationLoaderException.MSG,
                    err_code=ManeuverAuthorizationLoaderException.ERR_CODE,
                    ex=form_id_validation.exception,
                )
            )        
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant,
            target_model=ManeuverRequest,
            null_exception=ManeuverRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizationLoaderException.MSG,
                    err_code=ManeuverAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(ManeuverRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_APPLICANT_ID_ATTRIBUTE. ---#
        applicant_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if applicant_id_validation.is_failure:
            # Send an exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizationLoaderException.MSG,
                    err_code=ManeuverAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_id_validation.exception,
                )
            )
        # --- PROCESS_THE_TOKEN_APPLICANT_ATTRIBUTE. ---#
        token_validation = self._token_validation_service.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=applicant.traveler),
                id=IdFactory.next_id("ValidationRequest")
            )
        )
        # Handle the case that the applicant is not good Token.
        if token_validation.is_failure:
            # Send an exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizationLoaderException.MSG,
                    err_code=ManeuverAuthorizationLoaderException.ERR_CODE,
                    ex=token_validation.exception,
                )
            )
        # --- PROCESS_THE_PATH_APPLICANT_ATTRIBUTE. ---#
        path_validation = self._path_validation_service.extract_model(
            request=PathValidationRequest(
                item=PathCarrier(model=applicant.path),
                id=IdFactory.next_id("ValidationRequest")
            )
        )
        # Handle the case that the applicant is not safe Path.
        if path_validation.is_failure:
            # Send an exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizationLoaderException.MSG,
                    err_code=ManeuverAuthorizationLoaderException.ERR_CODE,
                    ex=path_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        token = cast(Token, token_validation.payload)
        path = cast(Path, path_validation.payload)
        transaction_id = cast(int, applicant_id_validation.payload)
        permission_id = cast(int, form_id_validation.payload)
        
        # --- Prepare a transaction approval. ---#
        approved_applicant = ManeuverRequest(
            traveler=token,
            path=path,
            id=transaction_id,
        )
        permission_request = ManeuverPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )
        



