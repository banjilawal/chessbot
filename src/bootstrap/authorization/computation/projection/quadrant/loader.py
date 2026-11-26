# src/bootstrap/authorization/projection/quadrant/loader.py

"""
Module: bootstrap.authorization.projection.quadrant.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import QuadrantProjectionDecision
from bootstrap import ProjectionAuthorizationLoader
from domain import Vector, VectorNode
from microservice import VectorValidationService
from request import (
    QuadrantProjectionPermissionRequest, QuadrantProjectionRequest, VectorNodeValidationRequest
)
from transit import VectorNodeCarrier
from util import IdFactory, LoggingLevelRouter


class QuadrantProjectionAuthorizationLoader(
    ProjectionAuthorizationLoader[QuadrantProjectionPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ModelAuthorizer
        
    Attributes:
        vector_validation_service: VectorValidationService
        
    Provides:
        -   def execute(candidate: Any) -> QuadrantProjectionDecision

    Super Class:
        ProjectionAuthorizationLoader
    """
    
    def __init__(self):
        """"""
        super().__init__()

    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> QuadrantProjectionDecision:
        """
        Checks if the Request is the right type.

        Action:
            1.  Send an exception chain in the Decision denial if any of the following
                occur.
                    -   The candidate is null or the wrong type.
                    -   The bundled transaction_request is null or the wrong type.
                    -   Validating either
                            -   quadrant_projection_request.node
                            -   quadrant_projection_request.x_step
                            -   quadrant_prjection_request.slope
                        fails.
                    -   The node is empty.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           QuadrantProjectionDecision
        Raises:
            QuadrantProjectionAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=QuadrantProjectionPermissionRequest,
            null_exception=QuadrantProjectionPermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return QuadrantProjectionDecision.denial(
                exception=QuadrantProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantProjectionAuthorizationLoaderException.MSG,
                    err_code=QuadrantProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(QuadrantProjectionPermissionRequest, priming.payload)
        
        # Handle the case that the permissio_form does not have an id.
        permission_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_id_validation.is_failure:
            # Send an exception chain in the denial.
            return QuadrantProjectionDecision.denial(
                exception=QuadrantProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantProjectionAuthorizationLoaderException.MSG,
                    err_code=QuadrantProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=permission_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant.,
            target_model=QuadrantProjectionRequest,
            null_exception=QuadrantProjectionRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return QuadrantProjectionDecision.denial(
                exception=QuadrantProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantProjectionAuthorizationLoaderException.MSG,
                    err_code=QuadrantProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(QuadrantProjectionRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_APPLICANT_ID_ATTRIBUTE. ---#
        transaction_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if transaction_id_validation.is_failure:
            # Send an exception chain in the denial.
            return QuadrantProjectionDecision.denial(
                exception=QuadrantProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantProjectionAuthorizationLoaderException.MSG,
                    err_code=QuadrantProjectionAuthorizationLoaderException.ERR_CODE,
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
            return QuadrantProjectionDecision.denial(
                exception=QuadrantProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantProjectionAuthorizationLoaderException.MSG,
                    err_code=QuadrantProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=node_validation.exception,
                )
            )
        # --- PROCESS_THE_SLOPE_AND_STEP_ATTRIBUTES. ---#
        line_properties = []
        for number in [applicant.x_step, applicant.slope]:
            number_validation = self.number_validator.execute(candidate=number)
            # Handle the case that the number is flagged.
            if number_validation.is_failure:
                # Send an exception chain in the denial.
                return QuadrantProjectionDecision.denial(
                    exception=QuadrantProjectionAuthorizationLoaderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=QuadrantProjectionAuthorizationLoaderException.MSG,
                        err_code=QuadrantProjectionAuthorizationLoaderException.ERR_CODE,
                        ex=number_validation.exception,
                    )
                )
            line_properties.append(cast(int, number_validation.payload))
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        node = cast(VectorNode, node_validation.payload)
        x_step = line_properties[0]
        slope = line_properties[1]
        transaction_id = cast(int, transaction_id_validation.payload)
        permission_id = cast(int, permission_id_validation.payload)
        
        # Handle the case that the node is empty.
        if node.is_empty:
            # Send an exception chain in the denial.
            return QuadrantProjectionDecision.denial(
                exception=QuadrantProjectionAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantProjectionAuthorizationLoaderException.MSG,
                    err_code=QuadrantProjectionAuthorizationLoaderException.ERR_CODE,
                    ex=EmptyVectorNodeException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyVectorNodeException.MSG,
                        err_code=EmptyVectorNodeException.ERR_CODE,
                    ),
                )
            )
        # --- Prepare a transaction approval. ---#
        approved_applicant = QuadrantProjectionRequest(
            node=node,
            x_step=x_step,
            slope=slope,
            id=transaction_id,
        )
        permission_request = QuadrantProjectionPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return QuadrantProjectionDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )