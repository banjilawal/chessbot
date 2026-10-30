# src/bootstrap/authorization/crud/insertion/account/loader.py

"""
Module: bootstrap.authorization.crud.insertion.account.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision
from authorization import InsertionAuthorizationLoader
from collection import AccountStack
from domain import Account
from err import (
    AccountPushPermissionLoaderException, CrudRequestNullException,
    PermissionRequestNullException
)
from exchange import (
    AccountPushPermissionRequest, AccountPushRequest, AccountValidationRequest,
    AccountValidationService
)
from transit import AccountCarrier
from util import IdFactory, LoggingLevelRouter


class AccountPushPermissionLoader(
    InsertionAuthorizationLoader[AccountPushPermissionRequest]
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
    
    def __init__(
            self,
            validation_service: Optional[AccountValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[AccountValidationService]
        """
        super().__init__(validation_service=validation_service or AccountValidationService())
    
    @property
    def validation_service(self) -> AccountValidationService:
        return cast(AccountValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: AccountPushPermissionRequest) -> Decision:
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
            null_exception=PermissionRequestNullException()
        )
        if priming.is_failure:
            # Send the exception chain in the denial.
            return Decision.denial(
                permission_request=candidate,
                exception=AccountPushPermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionLoaderException.MSG,
                    err_code=AccountPushPermissionLoaderException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate to a permission_request for additional processing. ---#
        permission_request = cast(
            AccountPushPermissionRequest,
            priming.authorization_applicant,
        )
        # Handle the case that permission_request.payload gets flagged.
        permission_payload_validation = self.priming_validator.execute(
            candidate=permission_request.authorization_applicant,
            target_model=AccountPushRequest,
            null_exception=CrudRequestNullException()
        )
        if permission_payload_validation.is_failure:
            # Send the exception chain in the denial.
            return Decision.denial(
                permission_request=permission_request,
                exception=AccountPushPermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionLoaderException.MSG,
                    err_code=AccountPushPermissionLoaderException.ERR_CODE,
                    ex=permission_payload_validation.exception
                )
            )
        # --- Cast permission_payload to an AccountPushRequest for field validation. ---#
        transaction_request = cast(
            AccountPushRequest,
            permission_payload_validation.authorization_applicant,
        )
        # Handle the case that the collection has an error.
        collection_validation = self.priming_validator.execute(
            candidate=transaction_request.collection,
            target_model=AccountStack,
            null_exception=AccountStackNullException(),
        )
        if collection_validation.is_failure:
            # Send the exception chain in the denial.
            return Decision.denial(
                permission_request=permission_request,
                exception=AccountPushPermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionLoaderException.MSG,
                    err_code=AccountPushPermissionLoaderException.ERR_CODE,
                    ex=collection_validation.exception
                )
            )
        # Handle the case that the transaction_request.item is not a valid account.
        item_validation = self.validation_service.extract_model(
            request=AccountValidationRequest(
                item=AccountCarrier(model=transaction_request.item),
                id=IdFactory.next_id(class_name="AccountValidationRequest")
            )
        )
        if item_validation.is_failure:
            # Send the exception chain in the denial.
            return Decision.denial(
                permission_request=candidate,
                exception=AccountPushPermissionLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionLoaderException.MSG,
                    err_code=AccountPushPermissionLoaderException.ERR_CODE,
                    ex=item_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        account = cast(Account, item_validation.payload)
        stack = cast(AccountStack, collection_validation.authorization_applicant)
        
        # --- Prepare an approval of the transaction. ---#
        transaction_request = AccountPushRequest(
            id=transaction_request.id,
            item=account,
            collection=stack,
        )
        # --- Forward the approval. ---#
        return Decision.grant(
            permission_request=candidate,
            approval=transaction_request,
        )