# src/authorization/permitter/crud/insertion/push.account//permitter.py

"""
Module: authorization.permitter.crud.insertion.push.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision
from authorization import AccountPushPermissionLoader, PushPermitter
from collection import AccountStack
from domain import Account
from err import ChessException, NullException
from exchange import (
    AccountPushPermissionRequest, AccountPushRequest, AccountValidationRequest,
    AccountValidationService
)
from transit import AccountCarrier
from util import IdFactory, LoggingLevelRouter


class AccountPushPermitter(PushPermitter[AccountPushPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Forward a decision about an AccountPushPermissionRequest to an 
            AccountPushPermitter.

    Attributes:
        validation_service: AccountValidationService
        loader: PushPermissionLoader
    Provides:
        -   def execute(request: AccountPushPermissionRequest) -> Decision

    Super Class:
        PushPermitter
    """

    
    def __init__(
            self,
            loader: Optional[AccountPushPermissionLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PushPermissionLoader]
        """
        super().__init__(loader=loader or AccountPushPermissionLoader())
    
    @property
    def loader(self) -> AccountPushPermissionLoader:
        return cast(AccountPushPermissionLoader, super().loader)
    
    @property
    def validation_service(self) -> AccountValidationService:
        return cast(AccountValidationService, super().validation_service)
        

    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushPermissionRequest) -> InsertionDecision:
        """
        Grant permission for a stack push.
        
        Args:
            request: AccountPushPermissionRequest
        Returns:
           Decision
        Raises:
            AccountPushPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request cannot be loaded.
        decision = self.loader.execute(candidate=request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return Decision.denial(
                permission_request=request,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        transaction_request = cast(AccountPushRequest, decision.approval)
        item = cast(Account, transaction_request.item)
        collection = cast(AccountStack, transaction_request.collection)
        
        if item in collection.items:
        
        
        permission_request = cast(AccountPushPermissionRequest, decision.permission_request)
        approval = cast(AccountPushRequest, decision.approval)
        
        priming_result = self.loader.priming_validator.execute(
            candidate=approval,
            target_model=AccountPushRequest,
            null_exception=NullException(),
        )
        if priming_result.is_failure:
            return Decision.denial(
                permission_request=permission_request,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        safe = cast(AccountPushRequest, priming_result.payload)
        
        item_validation = self.validation_service.extract_model(
            request=AccountValidationRequest(
                item=AccountCarrier(model=safe.item),
                id=IdFactory.next_id(class_name="AccountValidationRequest")
            )
        )
        if item_validation.is_failure:
            return Decision.denial(
                permission_request=permission_request,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=item_validation.exception,
                )
            )
        collection_validation = self.loader.priming_validator.execute(
            candidate=safe.collection,
            target_model=AccountStack,
            null_exception=NullException()
        )
        if collection_validation.is_failure:
            return Decision.denial(
                permission_request=permission_request,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=collection_validation.exception,
                )
            )
        account = cast(Account, item_validation.payload)
        stack = cast(AccountStack, collection_validation.payload)
        
        transaction_request = AccountPushRequest(
            id=safe.id,
            item=account,
            collection=stack,
        )
        decision = Decision.grant(
            permission_request=permission_request,
            approval=transaction_request,
        )
        return decision
        
        
        
        