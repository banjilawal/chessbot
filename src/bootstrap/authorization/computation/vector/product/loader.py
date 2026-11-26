# src/bootstrap/authorization/vectorproduct/loader.py

"""
Module: bootstrap.authorization.vector.product.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ScalarProductDecision
from bootstrap import VectorComputationAuthorizationLoader
from domain import Scalar, Vector
from microservice import ScalarValidationService, VectorValidationService
from transit import ScalarCarrier, VectorCarrier
from util import IdFactory, LoggingLevelRouter

class ScalarProductAuthorizationLoader(
    VectorComputationAuthorizationLoader[ScalarProductPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ModelAuthorizer
        
    Attributes:

    Provides:
        -   def execute(candidate: Any) -> ProductDecision

    Super Class:
        ProductAuthorizationLoader
    """
    _vector_validation_service: VectorValidationService
    _scalar_validation_service: ScalarValidationService
    
    def __init__(
            self,
            vector_validation_service: Optional[VectorValidationService] | None = None,
            scalar_validation_service: Optional[ScalarValidationService] | None = None,
    ):
        """
        Args:
            vector_validation_service: Optional[VectorValidationService]
            scalar_validation_service: Optional[ScalarValidationService]
        """
        super().__init__()
        self._vector_validation_service = (
                vector_validation_service or VectorValidationService()
        )
        self._scalar_validation_service = (
                scalar_validation_service or ScalarValidationService()
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ScalarProductDecision:
        """
        Checks if the Request is the right type.

        Action:
            1.  Send an exception chain in the Decision denial if any of the following
                occur.
                    -   The candidate is null or the wrong type.
                    -   The bundled transaction_request is null or the wrong type.
                    -   There is an error with transaction_request.collection
                    -   Validating transaction_request.scalar fails.
            2.  Otherwise, send an approval.
        Args:
            candidate: ScalarProductPermissionRequest
        Returns:
           Decision
        Raises:
            ScalarProductAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=ScalarProductPermissionRequest,
            null_exception=ScalarProductPermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return ScalarProductDecision.denial(
                exception=ScalarProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductAuthorizationLoaderException.MSG,
                    err_code=ScalarProductAuthorizationLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(
            ScalarProductPermissionRequest,
            priming.payload,
        )
        # Handle the case that the permissio_form does not have an id.
        permission_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_id_validation.is_failure:
            # Send an exception chain in the denial.
            return ScalarProductDecision.denial(
                exception=ScalarProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductAuthorizationLoaderException.MSG,
                    err_code=ScalarProductAuthorizationLoaderException.ERR_CODE,
                    ex=permission_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant.vector_applicant,
            target_model=ScalarProductRequest,
            null_exception=ScalarProductRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return ScalarProductDecision.denial(
                exception=ScalarProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductAuthorizationLoaderException.MSG,
                    err_code=ScalarProductAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(ScalarProductRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_APPLICANT_ID_ATTRIBUTE. ---#
        transaction_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if transaction_id_validation.is_failure:
            # Send an exception chain in the denial.
            return ScalarProductDecision.denial(
                exception=ScalarProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductAuthorizationLoaderException.MSG,
                    err_code=ScalarProductAuthorizationLoaderException.ERR_CODE,
                    ex=transaction_id_validation.exception,
                )
            )
        # --- PROCESS_THE_VECTTOR_CANDIDATE_ATTRIBUTE. ---#
        vector_validation = self._vector_validation_service.extract_model(
            request=VectorValidationRequest(
                item=VectorCarrier(model=applicant.origin),
                id=IdFactory.next_id("ValidationRequest")
            )
        )
        # Handle the case that the applicant is not Scalar.
        if vector_validation.is_failure:
            # Send an exception chain in the denial.
            return ScalarProductDecision.denial(
                exception=ScalarProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductAuthorizationLoaderException.MSG,
                    err_code=ScalarProductAuthorizationLoaderException.ERR_CODE,
                    ex=vector_validation.exception,
                )
            )
        # --- PROCESS_THE_SCALAR_CANDIDATE_ATTRIBUTE. ---#
        scalar_validation = self._scalar_validation_service.extract_model(
            request=ScalarValidationRequest(
                item=ScalarCarrier(model=applicant.scalar),
                id=IdFactory.next_id("ValidationRequest")
            )
        )
        # Handle the case that the applicant is not Scalar.
        if scalar_validation.is_failure:
            # Send an exception chain in the denial.
            return ScalarProductDecision.denial(
                exception=ScalarProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductAuthorizationLoaderException.MSG,
                    err_code=ScalarProductAuthorizationLoaderException.ERR_CODE,
                    ex=scalar_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        vector = cast(Vector, vector_validation.payload)
        scalar = cast(Scalar, scalar_validation.payload)
        transaction_id = cast(int, transaction_id_validation.payload)
        permission_id = cast(int, permission_id_validation.payload)
        
        # --- Prepare a transaction approval. ---#
        approved_applicant = ScalarProductRequest(
            vector=vector,
            scalar=scalar,
            id=transaction_id,
        )
        permission_request = ScalarProductPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return ScalarProductDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )