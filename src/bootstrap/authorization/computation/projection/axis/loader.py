# src/bootstrap/authorization/projection/axis/loader.py

"""
Module: bootstrap.authorization.projection.axis.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AxisProjectionDecision
from bootstrap import ProjectionAuthorizationLoader
from domain import Vector, VectorNode
from microservice import VectorValidationService
from request import (
    AxisProjectionPermissionRequest, AxisProjectionRequest, VectorNodeValidationRequest
)
from transit import VectorNodeCarrier
from util import IdFactory, LoggingLevelRouter


class AxisProjectionAuthorizationLoader(
    ProjectionAuthorizationLoader[AxisProjectionPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ModelAuthorizer
        
    Attributes:
        vector_validation_service: VectorValidationService
        
    Provides:
        -   def execute(candidate: Any) -> AxisDecision

    Super Class:
        ProjectionAuthorizationLoader
    """

    _vector_validation_service: VectorValidationService
    
    def __init__(
            self,
            vector_validation_service: Optional[VectorValidationService] | None = None,
    ):
        """
        Args:
            vector_validation_service: Optional[VectorValidationService]
        """
        super().__init__()
        self._vector_validation_service = vector_validation_service or VectorValidationService()
        
    @property
    def vector_validation_service(self) -> VectorValidationService:
        return self._vector_validation_service
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AxisProjectionDecision:
        """
        Checks if the Request is the right type.

        Action:
            1.  Send an exception chain in the Decision denial if any of the following
                occur.
                    -   The candidate is null or the wrong type.
                    -   The bundled transaction_request is null or the wrong type.
                    -   Validating either
                            -   axis_projection_request.node
                            -   axis_projection_request.delta
                        fails.
                    -   The node is empty..
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           AxisProjectionDecision
        Raises:
            AxisProjectionAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=AxisProjectionPermissionRequest,
            null_exception=AxisProjectionPermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return AxisProjectionDecision.denial(
                exception=AxisProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisProjectionAuthorizationLoaderException.MSG,
                    err_code=AxisProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(AxisProjectionPermissionRequest, priming.payload)
        
        # Handle the case that the permissio_form does not have an id.
        permission_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_id_validation.is_failure:
            # Send an exception chain in the denial.
            return AxisProjectionDecision.denial(
                exception=AxisProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisProjectionAuthorizationLoaderException.MSG,
                    err_code=AxisProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=permission_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant.,
            target_model=AxisProjectionRequest,
            null_exception=AxisProjectionRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return AxisProjectionDecision.denial(
                exception=AxisProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisProjectionAuthorizationLoaderException.MSG,
                    err_code=AxisProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(AxisProjectionRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_APPLICANT_ID_ATTRIBUTE. ---#
        transaction_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if transaction_id_validation.is_failure:
            # Send an exception chain in the denial.
            return AxisProjectionDecision.denial(
                exception=AxisProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisProjectionAuthorizationLoaderException.MSG,
                    err_code=AxisProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=transaction_id_validation.exception,
                )
            )
        # --- PROCESS_THE_VECTTOR_NODE_CANDIDATE_ATTRIBUTE. ---#
        node_validation = self.node_validation_service.extract_model(
            request=VectorNodeValidationRequest(
                item=VectorNodeCarrier(model=applicant.node),
                id=IdFactory.next_id(class_name="Request")
            )
        )
        # Handle the case that the node is flagged.
        if node_validation.is_failure:
            # Send an exception chain in the denial.
            return AxisProjectionDecision.denial(
                exception=AxisProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisProjectionAuthorizationLoaderException.MSG,
                    err_code=AxisProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=node_validation.exception,
                )
            )
        # --- PROCESS_THE_DELTA_CANDIDATE_ATTRIBUTE. ---#
        delta_validation = self.vector_validation_service.extract_model(
            request=VectorValidationRequest(
                item=VectorCarrier(model=applicant.delta),
                id=IdFactory.next_id(class_name="Request")
            )
        )
        # Handle the case that the delta is flagged.
        if delta_validation.is_failure:
            # Send an exception chain in the denial.
            return AxisProjectionDecision.denial(
                exception=AxisProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisProjectionAuthorizationLoaderException.MSG,
                    err_code=AxisProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=delta_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        node = cast(VectorNode, node_validation.payload)
        delta = cast(Vector, delta_validation.payload)
        transaction_id = cast(int, transaction_id_validation.payload)
        permission_id = cast(int, permission_id_validation.payload)
        
        # Handle the case that the node is empty.
        if node.is_empty:
            # Send an exception chain in the denial.
            return AxisProjectionDecision.denial(
                exception=AxisProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisProjectionAuthorizationLoaderException.MSG,
                    err_code=AxisProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=EmptyVectorNodeException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyVectorNodeException.MSG,
                        err_code=EmptyVectorNodeException.ERR_CODE,
                    ),
                )
            )
        # --- Prepare a transaction approval. ---#
        approved_applicant = AxisProjectionRequest(
            node=node,
            delta=delta,
            id=transaction_id,
        )
        permission_request = AxisProjectionPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return AxisProjectionDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )