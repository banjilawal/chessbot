# src/bootstrap/authorization/distance/loader.py

"""
Module: bootstrap.authorization.distance.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, Optional, cast

from artifcat import DistanceComputationDecision
from bootstrap import ComputationAuthorizationLoader
from domain import Vector
from exchange import (
    DistanceComputationPermissionRequest, VectorDistanceRequest, VectorValidationRequest
)
from microservice import VectorValidationService
from transit import VectorCarrier
from util import IdFactory, LoggingLevelRouter

class DistanceComputationAuthorizationLoader(
    ComputationAuthorizationLoader[DistanceComputationPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ModelAuthorizer
        
    Attributes:

    Provides:
        -   def execute(candidate: Any) -> DistanceDecision

    Super Class:
        DistanceAuthorizationLoader
    """
    _validation_service: VectorValidationService
    
    def __init__(
            self,
            validation_service: Optional[VectorValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[VectorValidationService]
        """
        super().__init__()
        self._validation_service = validation_service or VectorValidationService()
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> DistanceComputationDecision:
        """
        Checks if the Request is the right type.

        Action:
            1.  Send an exception chain in the Decision denial if any of the following
                occur.
                    -   The candidate is null or the wrong type.
                    -   The bundled transaction_request is null or the wrong type.
                    -   There is an error with transaction_request.collection
                    -   Validating transaction_request.vector fails.
            2.  Otherwise, send an approval.
        Args:
            candidate: DistanceComputationPermissionRequest
        Returns:
           Decision
        Raises:
            DistanceComputationAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=DistanceComputationPermissionRequest,
            null_exception=DistanceComputationPermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return DistanceComputationDecision.denial(
                exception=DistanceComputationAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DistanceComputationAuthorizationLoaderException.MSG,
                    err_code=DistanceComputationAuthorizationLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_form for distanceal processing. ---#
        permission_form = cast(
            DistanceComputationPermissionRequest,
            priming.payload,
        )
        # Handle the case that the permissio_form does not have an id.
        permission_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_id_validation.is_failure:
            # Send an exception chain in the denial.
            return DistanceComputationDecision.denial(
                exception=DistanceComputationAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DistanceComputationAuthorizationLoaderException.MSG,
                    err_code=DistanceComputationAuthorizationLoaderException.ERR_CODE,
                    ex=permission_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant,
            target_model=VectorDistanceRequest,
            null_exception=VectorDistanceRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return DistanceComputationDecision.denial(
                exception=DistanceComputationAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DistanceComputationAuthorizationLoaderException.MSG,
                    err_code=DistanceComputationAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(VectorDistanceRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_APPLICANT_ID_ATTRIBUTE. ---#
        transaction_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if transaction_id_validation.is_failure:
            # Send an exception chain in the denial.
            return DistanceComputationDecision.denial(
                exception=DistanceComputationAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DistanceComputationAuthorizationLoaderException.MSG,
                    err_code=DistanceComputationAuthorizationLoaderException.ERR_CODE,
                    ex=transaction_id_validation.exception,
                )
            )
        # --- PROCESS_THE_VECTTOR_CANDIDATE_ATTRIBUTE. ---#
        vectors: List[Vector] = []
        for candidate in [applicant.u, applicant.v]:
            validation = self._validation_service.extract_model(
                request=VectorValidationRequest(
                    item=VectorCarrier(model=candidate),
                    id=IdFactory.next_id("ValidationRequest")
                )
            )
            # Handle the case that the applicant is not Vector.
            if validation.is_failure:
                # Send an exception chain in the denial.
                return DistanceComputationDecision.denial(
                    exception=DistanceComputationAuthorizationLoaderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DistanceComputationAuthorizationLoaderException.MSG,
                        err_code=DistanceComputationAuthorizationLoaderException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            vectors.append(cast(Vector, validation.payload))
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        u = vectors[0]
        v = vectors[1]
        transaction_id = cast(int, transaction_id_validation.payload)
        permission_id = cast(int, permission_id_validation.payload)
        
        # --- Prepare a transaction approval. ---#
        approved_applicant = VectorDistanceRequest(
            u=u,
            v=v,
            id=transaction_id,
        )
        permission_request = DistanceComputationPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return DistanceComputationDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )