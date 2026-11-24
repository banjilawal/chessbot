# src/bootstrap/authorization/crud/insertion/add/vector/loader.py

"""
Module: bootstrap.authorization.crud.insertion.add.vector.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AddVectorNodeDecision
from bootstrap import AddNodeAuthorizationLoader
from collection import VectorChain
from domain import VectorNode
from err import VectorChainNullException
from microservice import VectorNodeValidationService
from request import (
    AddVectorNodePermissionRequest, AddVectorNodeRequest, VectorNodeValidationRequest
)
from transit import VectorNodeCarrier
from util import IdFactory, LoggingLevelRouter


class AddVectorNodeAuthorizationLoader(
    AddNodeAuthorizationLoader[AddVectorNodePermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a CrudAuthorization module.

    Attributes:
        validation_service: VectorNodeValidationService

    Super Class:
        InsertionAuthorizationLoader
    """
    
    _validation_service: VectorNodeValidationService
    
    def __init__(
            self,
            validation_service: Optional[VectorNodeValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[VectorNodeValidationService]
        """
        super().__init__()
        self._validation_service = validation_service or VectorNodeValidationService()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AddVectorNodeDecision:
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
            candidate: AddVectorNodePermissionRequest
        Returns:
           Decision
        Raises:
            AddVectorNodePermissionLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=AddVectorNodePermissionRequest,
            null_exception=AddVectorNodePermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return AddVectorNodeDecision.denial(
                exception=AddVectorNodePermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodePermissionLoaderException.MSG,
                    err_code=AddVectorNodePermissionLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(
            AddVectorNodePermissionRequest,
            priming.payload,
        )
        # Handle the case that the permission_form does not have an id.
        permission_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_id_validation.is_failure:
            # Send an exception chain in the denial.
            return AddVectorNodeDecision.denial(
                exception=AddVectorNodeAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodeAuthorizationLoaderException.MSG,
                    err_code=AddVectorNodeAuthorizationLoaderException.ERR_CODE,
                    ex=permission_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant,
            target_model=AddVectorNodeRequest,
            null_exception=AddVectorNodeRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return AddVectorNodeDecision.denial(
                exception=AddVectorNodeAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodeAuthorizationLoaderException.MSG,
                    err_code=AddVectorNodeAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(AddVectorNodeRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_TRANSACTION_ID_ATTRIBUTE. ---#
        transaction_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if transaction_id_validation.is_failure:
            # Send an exception chain in the denial.
            return AddVectorNodeDecision.denial(
                exception=AddVectorNodeAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodeAuthorizationLoaderException.MSG,
                    err_code=AddVectorNodeAuthorizationLoaderException.ERR_CODE,
                    ex=transaction_id_validation.exception,
                )
            )
        # --- PROCESS_THE_VECTOR_ADD_ITEM_ATTRIBUTE. ---#
        item_validation = self._validation_service.extract_model(
            request=VectorNodeValidationRequest(
                item=VectorNodeCarrier(model=applicant.item),
                id=IdFactory.next_id("Request")
            )
        )
        # Handle the case that the applicant is not Vector.
        if item_validation.is_failure:
            # Send an exception chain in the denial.
            return AddVectorNodeDecision.denial(
                exception=AddVectorNodeAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodeAuthorizationLoaderException.MSG,
                    err_code=AddVectorNodeAuthorizationLoaderException.ERR_CODE,
                    ex=item_validation.exception,
                )
            )
        # --- PROCESS_THE_VECTOR_ADD_COLLECTION_ATTRIBUTE. ---#
        collection_validation = self.priming_validator.execute(
            candidate=applicant.collection,
            target_model=VectorChain,
            null_exception=VectorChainNullException()
        )
        # Handle the case that the vector_add collection is not safe.
        if collection_validation.is_failure:
            # Send an exception chain in the denial.
            return AddVectorNodeDecision.denial(
                exception=AddVectorNodeAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodeAuthorizationLoaderException.MSG,
                    err_code=AddVectorNodeAuthorizationLoaderException.ERR_CODE,
                    ex=collection_validation.exception
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        item = cast(VectorNode, item_validation.payload)
        collection = cast(VectorChain, collection_validation.payload)
        transaction_id = cast(int, transaction_id_validation.payload)
        permission_id = cast(int, permission_id_validation.payload)
        
        # --- Prepare a transaction approval. ---#
        approved_applicant = AddVectorNodeRequest(
            item=item,
            collection=collection,
            id=transaction_id,
        )
        permission_request = AddVectorNodePermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return AddVectorNodeDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )
