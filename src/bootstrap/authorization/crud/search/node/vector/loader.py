# src/bootstrap/authorization/crud/search/node/vector/loader.py

"""
Module: bootstrap.authorization.crud.search.node.vector.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import VectorNodeSearchDecision
from bootstrap import NodeSearchAuthorizationLoader

from collection import VectorChain
from domain import VectorNodeContext
from err import (
    VectorNodeSearchAuthorizationLoaderException, VectorNodeSearchPermissionRequestNullException,
    VectorNodeSearchRequestNullException, VectorChainNullException,
)
from request import VectorNodeSearchPermissionRequest, VectorNodeSearchRequest
from util import IdFactory, LoggingLevelRouter


class VectorNodeNodeSearchAuthorizationLoader(
    NodeSearchAuthorizationLoader[VectorNodeSearchPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a CrudAuthorization module.

    Attributes:
        validation_service: VectorNodeContextValidationService

    Super Class:
        SearchAuthorizationLoader
    """
    
    _validation_service: VectorNodeContextValidationService
    
    def __init__(
            self,
            validation_service: Optional[VectorNodeContextValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[VectorNodeContextValidationService]
        """
        super().__init__()
        self._validation_service = validation_service or VectorNodeContextValidationService()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> VectorNodeSearchDecision:
        """
        Checks if the Request is the right type.

        Action:
            1.  Send an exception chain in the Decision denial if any of the following
                occur.
                    -   The candidate is null or the wrong type.
                    -   The bundled transaction_request is null or the wrong type.
                    -   There is an error with transaction_request.collection
                    -   Validating transaction_request.context fails.
            2.  Otherwise, send an approval.
        Args:
            candidate: VectorNodeSearchPermissionRequest
        Returns:
           Decision
        Raises:
            VectorNodeSearchAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=VectorNodeSearchPermissionRequest,
            null_exception=VectorNodeSearchPermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return VectorNodeSearchDecision.denial(
                exception=VectorNodeSearchAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchAuthorizationLoaderException.MSG,
                    err_code=VectorNodeSearchAuthorizationLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(
            VectorNodeSearchPermissionRequest,
            priming.payload,
        )
        # Handle the case that the permissio_form does not have an id.
        permission_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_id_validation.is_failure:
            # Send an exception chain in the denial.
            return VectorNodeSearchDecision.denial(
                exception=VectorNodeSearchAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchAuthorizationLoaderException.MSG,
                    err_code=VectorNodeSearchAuthorizationLoaderException.ERR_CODE,
                    ex=permission_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant,
            target_model=VectorNodeSearchRequest,
            null_exception=VectorNodeSearchRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return VectorNodeSearchDecision.denial(
                exception=VectorNodeSearchAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchAuthorizationLoaderException.MSG,
                    err_code=VectorNodeSearchAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(VectorNodeSearchRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_APPLICANT_ID_ATTRIBUTE. ---#
        transaction_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if transaction_id_validation.is_failure:
            # Send an exception chain in the denial.
            return VectorNodeSearchDecision.denial(
                exception=VectorNodeSearchAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchAuthorizationLoaderException.MSG,
                    err_code=VectorNodeSearchAuthorizationLoaderException.ERR_CODE,
                    ex=transaction_id_validation.exception,
                )
            )
        # --- PROCESS_THE_VECTORNODE_CANDIDATE_ATTRIBUTE. ---#
        context_validation = self._validation_service.extract_node(
            request=VectorNodeContextValidationRequest(
                item=VectorNodeContextCarrier(node=applicant.context),
                id=IdFactory.next_id("Request")
            )
        )
        # Handle the case that the applicant is not VectorNode.
        if context_validation.is_failure:
            # Send an exception chain in the denial.
            return VectorNodeSearchDecision.denial(
                exception=VectorNodeSearchAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchAuthorizationLoaderException.MSG,
                    err_code=VectorNodeSearchAuthorizationLoaderException.ERR_CODE,
                    ex=context_validation.exception,
                )
            )
        # --- PROCESS_THE_VECTORNODE_COLLECTION_ATTRIBUTE. ---#
        collection_validation = self.priming_validator.execute(
            candidate=applicant.collection,
            target_model=VectorChain,
            null_exception=VectorChainNullException()
        )
        # Handle the case that the vectorNode_node collection is not safe.
        if collection_validation.is_failure:
            # Send an exception chain in the denial.
            return VectorNodeSearchDecision.denial(
                exception=VectorNodeSearchAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchAuthorizationLoaderException.MSG,
                    err_code=VectorNodeSearchAuthorizationLoaderException.ERR_CODE,
                    ex=collection_validation.exception
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        context = cast(VectorNodeContext, context_validation.payload)
        collection = cast(VectorChain, collection_validation.payload)
        transaction_id = cast(int, transaction_id_validation.payload)
        permission_id = cast(int, permission_id_validation.payload)
        
        # --- Prepare a transaction approval. ---#
        approved_applicant = VectorNodeSearchRequest(
            context=context,
            collection=collection,
            id=transaction_id,
        )
        permission_request = VectorNodeSearchPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return VectorNodeSearchDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )
