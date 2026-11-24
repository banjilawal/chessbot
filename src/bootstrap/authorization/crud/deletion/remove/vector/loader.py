# src/bootstrap/authorization/crud/deletion/vector/loader.py

"""
Module: bootstrap.authorization.crud.deletion.vector.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RemoveVectorNodeDecision
from bootstrap import RemoveNodeAuthorizationLoader
from collection import VectorChain
from domain import VectorNodeContext
from err import (
    RemoveVectorNodePermissionLoaderException, VectorChainNullException
)
from request import RemoveVectorNodePermissionRequest, RemoveVectorNodeRequest
from util import IdFactory, LoggingLevelRouter


class RemoveVectorNodePermissionLoader(
    RemoveNodeAuthorizationLoader[RemoveVectorNodePermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a CrudAuthorization module.

    Attributes:
        validation_service: VectorNodeContextValidationService

    Super Class:
        RemoveNodeAuthorizationLoader
    """
    
    def __init__(
            self,
            validation_service: Optional[VectorNodeContextValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[VectorNodeContextValidationService]
        """
        super().__init__(validation_service=validation_service or VectorNodeContextValidationService())
    
    @property
    def validation_service(self) -> VectorNodeContextValidationService:
        return cast(VectorNodeContextValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: RemoveVectorNodePermissionRequest) -> RemoveVectorNodeDecision:
        """
        Checks if the Request is the right type.

        Action:
            1.  Send an exception chain in the Decision denial if any of the following
                occur.
                    -   The candidate is null or the wrong type.
                    -   The bundled transaction_request is null or the wrong type.
                    -   There is an error with transaction_request.collection
                    -   Validating transaction_request.item fails.
            2.  Otherwise, send an approval.
        Args:
            candidate: RemoveVectorNodePermissionRequest
        Returns:
           Decision
        Raises:
            RemoveVectorNodePermissionLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=RemoveVectorNodePermissionRequest,
            null_exception=PermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return RemoveVectorNodeDecision.denial(
                exception=RemoveVectorNodePermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveVectorNodePermissionLoaderException.MSG,
                    err_code=RemoveVectorNodePermissionLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_request for additional processing. ---#
        permission_request = cast(
            RemoveVectorNodePermissionRequest,
            priming.payload,
        )
        # Handle the case that permission_request.payload gets flagged.
        permission_payload_validation = self.priming_validator.execute(
            candidate=permission_request.authorization_applicant,
            target_model=RemoveVectorNodeRequest,
            null_exception=CrudRequestNullException()
        )
        if permission_payload_validation.is_failure:
            # Send the exception chain in the denial.
            return RemoveVectorNodeDecision.denial(
                exception=RemoveVectorNodePermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveVectorNodePermissionLoaderException.MSG,
                    err_code=RemoveVectorNodePermissionLoaderException.ERR_CODE,
                    ex=permission_payload_validation.exception
                )
            )
        # --- Cast permission_payload to an RemoveVectorNodeRequest for field validation. ---#
        transaction_request = cast(
            RemoveVectorNodeRequest,
            permission_payload_validation.payload,
        )
        # Handle the case that the collection has an error.
        collection_validation = self.priming_validator.execute(
            candidate=transaction_request.collection,
            target_model=VectorChain,
            null_exception=VectorChainNullException(),
        )
        if collection_validation.is_failure:
            # Send the exception chain in the denial.
            return RemoveVectorNodeDecision.denial(
                exception=RemoveVectorNodePermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveVectorNodePermissionLoaderException.MSG,
                    err_code=RemoveVectorNodePermissionLoaderException.ERR_CODE,
                    ex=collection_validation.exception
                )
            )
        # Handle the case that the transaction_request.item is not a valid vector.
        context_validation = self.validation_service.extract_model(
            request=VectorNodeContextValidationRequest(
                item=VectorNodeContextCarrier(model=transaction_request.context),
                id=IdFactory.next_id(class_name="Request")
            )
        )
        if context_validation.is_failure:
            # Send the exception chain in the denial.
            return RemoveVectorNodeDecision.denial(
                exception=RemoveVectorNodePermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveVectorNodePermissionLoaderException.MSG,
                    err_code=RemoveVectorNodePermissionLoaderException.ERR_CODE,
                    ex=context_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        context = cast(VectorNodeContext, context_validation.payload)
        chain = cast(VectorChain, collection_validation.payload)
        
        # --- Prepare an approval of the transaction. ---#
        transaction_request = RemoveVectorNodeRequest(
            id=transaction_request.id,
            context=context,
            collection=chain,
        )
        # --- Forward the approval. ---#
        return RemoveVectorNodeDecision.grant(
            permission_request=candidate,
            transaction_request=transaction_request,
        )