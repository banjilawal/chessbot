# src/bootstrap/authorization/computation/product/model/account/loader.py

"""
Module: bootstrap.authorization.computation.product.model.account.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountProductDecision
from bootstrap import ModelScalarProductAuthorizationLoader
from collection import AccountStack
from domain import Account
from err import (
    AccountProductAuthorizationLoaderException, AccountProductPermissionRequestNullException,
    AccountProductRequestNullException, AccountStackNullException,
)
from exchange import (
    AccountContextValidationService, AccountProductRequest, AccountProductPermissionRequest,
    AccountContextValidationRequest,
)
from transit import AccountContextCarrier
from util import IdFactory, LoggingLevelRouter


class AccountProductAuthorizationLoader(
    ModelScalarProductAuthorizationLoader[AccountProductPermissionRequest]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ComputationAuthorization module.

    Attributes:
        validation_service: AccountContextValidationService

    Super Class:
        ProductAuthorizationLoader
    """
    
    _validation_service: AccountContextValidationService
    
    def __init__(
            self,
            validation_service: Optional[AccountContextValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[AccountContextValidationService]
        """
        super().__init__()
        self._validation_service = validation_service or AccountContextValidationService()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AccountProductDecision:
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
            candidate: AccountProductPermissionRequest
        Returns:
           Decision
        Raises:
            AccountProductAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=AccountProductPermissionRequest,
            null_exception=AccountProductPermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return AccountProductDecision.denial(
                exception=AccountProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountProductAuthorizationLoaderException.MSG,
                    err_code=AccountProductAuthorizationLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(
            AccountProductPermissionRequest,
            priming.payload,
        )
        # Handle the case that the permissio_form does not have an id.
        permission_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_id_validation.is_failure:
            # Send an exception chain in the denial.
            return AccountProductDecision.denial(
                exception=AccountProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountProductAuthorizationLoaderException.MSG,
                    err_code=AccountProductAuthorizationLoaderException.ERR_CODE,
                    ex=permission_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant,
            target_model=AccountProductRequest,
            null_exception=AccountProductRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return AccountProductDecision.denial(
                exception=AccountProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountProductAuthorizationLoaderException.MSG,
                    err_code=AccountProductAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(AccountProductRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_APPLICANT_ID_ATTRIBUTE. ---#
        transaction_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if transaction_id_validation.is_failure:
            # Send an exception chain in the denial.
            return AccountProductDecision.denial(
                exception=AccountProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountProductAuthorizationLoaderException.MSG,
                    err_code=AccountProductAuthorizationLoaderException.ERR_CODE,
                    ex=transaction_id_validation.exception,
                )
            )
        # --- PROCESS_THE_ACCOUNT_CANDIDATE_ATTRIBUTE. ---#
        context_validation = self._validation_service.extract_model(
            request=AccountContextValidationRequest(
                item=AccountContextCarrier(model=applicant.context),
                id=IdFactory.next_id("ValidationRequest")
            )
        )
        # Handle the case that the applicant is not Account.
        if context_validation.is_failure:
            # Send an exception chain in the denial.
            return AccountProductDecision.denial(
                exception=AccountProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountProductAuthorizationLoaderException.MSG,
                    err_code=AccountProductAuthorizationLoaderException.ERR_CODE,
                    ex=context_validation.exception,
                )
            )
        # --- PROCESS_THE_ACCOUNT_COLLECTION_ATTRIBUTE. ---#
        collection_validation = self.priming_validator.execute(
            candidate=applicant.collection,
            target_model=AccountStack,
            null_exception=AccountStackNullException()
        )
        # Handle the case that the account_model collection is not safe.
        if collection_validation.is_failure:
            # Send an exception chain in the denial.
            return AccountProductDecision.denial(
                exception=AccountProductAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountProductAuthorizationLoaderException.MSG,
                    err_code=AccountProductAuthorizationLoaderException.ERR_CODE,
                    ex=collection_validation.exception
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        context = cast(Account, context_validation.payload)
        collection = cast(AccountStack, collection_validation.payload)
        transaction_id = cast(int, transaction_id_validation.payload)
        permission_id = cast(int, permission_id_validation.payload)
        
        # --- Prepare a transaction approval. ---#
        approved_applicant = AccountProductRequest(
            context=context,
            collection=collection,
            id=transaction_id,
        )
        permission_request = AccountProductPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return AccountProductDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )
