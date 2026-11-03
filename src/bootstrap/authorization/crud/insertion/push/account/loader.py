# src/bootstrap/authorization/crud/insertion/push/account/loader.py

"""
Module: bootstrap.authorization.crud.insertion.push.account.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountPushDecision
from bootstrap import PushAuthorizationLoader
from collection import AccountStack
from domain import Account
from exchange import (
    AccountPushRequest, AccountPushPermissionRequest, AccountValidationRequest,
    AccountValidationService
)
from transit import AccountCarrier
from util import IdFactory, LoggingLevelRouter


class AccountPushAuthorizationLoader(
    PushAuthorizationLoader[AccountPushPermissionRequest]
):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a CrudAuthorization module.

    Attributes:
        validation_service: AccountValidationService

    Super Class:
        InsertionAuthorizationLoader
    """
    
    _validation_service: AccountValidationService
    
    def __init__(
            self,
            validation_service: Optional[AccountValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[AccountValidationService]
        """
        super().__init__()
        self._validation_service = validation_service or AccountValidationService()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AccountPushDecision:
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
            candidate: AccountPushPermissionRequest
        Returns:
           Decision
        Raises:
            AccountPushPermissionLoaderException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that priming is not completed.
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=AccountPushPermissionRequest,
            null_exception=AccountPermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushPermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionLoaderException.MSG,
                    err_code=AccountPushPermissionLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_form for additional processing. ---#
        permission_form = cast(
            AccountPushPermissionRequest,
            priming.payload,
        )
        # Handle the case that the permission_form does not have an id.
        permission_id_validation = self.identity_service.validate_id(
            candidate=permission_form.id
        )
        if permission_id_validation.is_failure:
            # Send an exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushAuthorizationLoaderException.MSG,
                    err_code=AccountPushAuthorizationLoaderException.ERR_CODE,
                    ex=permission_id_validation.exception,
                )
            )
        # Handle the case that the applicant signature is wrong.
        applicant_signature = self.priming_validator.execute(
            candidate=permission_form.authorization_applicant,
            target_model=AccountPushRequest,
            null_exception=AccountPushRequestNullException()
        )
        if applicant_signature.is_failure:
            # Send an exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushAuthorizationLoaderException.MSG,
                    err_code=AccountPushAuthorizationLoaderException.ERR_CODE,
                    ex=applicant_signature.exception,
                )
            )
        # --- Get the permission_request for type checking the applicant. ---#
        applicant = cast(AccountPushRequest, applicant_signature.payload)
        
        # --- PROCESS_THE_TRANSACTION_ID_ATTRIBUTE. ---#
        transaction_id_validation = self.identity_service.validate_id(applicant.id)
        # Handle the case that the id is not a number.
        if transaction_id_validation.is_failure:
            # Send an exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushAuthorizationLoaderException.MSG,
                    err_code=AccountPushAuthorizationLoaderException.ERR_CODE,
                    ex=transaction_id_validation.exception,
                )
            )
        # --- PROCESS_THE_ACCOUNT_PUSH_ITEM_ATTRIBUTE. ---#
        item_validation = self._validation_service.extract_model(
            request=AccountValidationRequest(
                item=AccountCarrier(model=applicant.item),
                id=IdFactory.next_id("AccountValidationRequest")
            )
        )
        # Handle the case that the applicant is not Account.
        if item_validation.is_failure:
            # Send an exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushAuthorizationLoaderException.MSG,
                    err_code=AccountPushAuthorizationLoaderException.ERR_CODE,
                    ex=item_validation.exception,
                )
            )
        # --- PROCESS_THE_ACCOUNT_PUSH_COLLECTION_ATTRIBUTE. ---#
        collection_validation = self.priming_validator.execute(
            candidate=applicant.collection,
            target_model=AccountStack,
            null_exception=AccountStackNullException()
        )
        # Handle the case that the account_push collection is not safe.
        if collection_validation.is_failure:
            # Send an exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushAuthorizationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushAuthorizationLoaderException.MSG,
                    err_code=AccountPushAuthorizationLoaderException.ERR_CODE,
                    ex=collection_validation.exception
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        item = cast(Account, item_validation.payload)
        collection = cast(AccountStack, collection_validation.payload)
        transaction_id = cast(int, transaction_id_validation.payload)
        permission_id = cast(int, permission_id_validation.payload)
        
        # --- Prepare a transaction approval. ---#
        approved_applicant = AccountPushRequest(
            item=item,
            collection=collection,
            id=transaction_id,
        )
        permission_request = AccountPushPermissionRequest(
            id=permission_id,
            authorization_applicant=approved_applicant,
        )
        # --- Forward the approval. ---#
        return AccountPushDecision.grant(
            transaction_request=approved_applicant,
            permission_request=permission_request,
        )
