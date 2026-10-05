# src/exchange/wrapper/validation/model/account/wrapper.py

"""
Module: exchange.wrapper.validation.model.account.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AccountValidationResponse, ValidationResult
from domain import Account, AccountBlueprint
from err import AccountValidationResponderException, AccountValidationResponseWrapperException, EmptyAccountCarrierException
from exchange import (
    AccountValidationResponder, ModelValidationResponseWrapper, AccountValidationRequest
)
from util import LoggingLevelRouter


class AccountValidationResponseWrapper(
    ModelValidationResponseWrapper[Account]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Account
                _   AccountBlueprint
            products from AccountValidationResponder.

    Attributes:
        responder: AccountValidationResponder
        
    Provides:
        -   def extract_model(
                    request: AccountValidationRequest
            ) -> ValidationResult[Account]
            
        -   def extract_blueprint(
                    request: AccountValidationRequest
            ) -> ValidationResult[AccountBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[AccountValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[AccountValidationResponder]
        """
        super().__init__(responder=responder or AccountValidationResponder())
    
    @property
    def responder(self) -> AccountValidationResponder:
        return cast(AccountValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: AccountValidationRequest,
    ) -> ValidationResult[Account]:
        """
        Extract a Account safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Account from the success response then send it 
                to the client.
        Args:
            request: AccountValidationRequest
        Result:
            ValidationResult[Account]
        Raises:
            AccountValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationResponseWrapperException.MSG,
                    err_code=AccountValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AccountValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationResponderException.MSG,
                    err_code=AccountValidationResponderException.ERR_CODE,
                    ex=EmptyAccountCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAccountCarrierException.MSG,
                        err_code=EmptyAccountCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Account, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AccountValidationRequest,
    ) -> ValidationResult[AccountBlueprint]:
        """
        Extract a AccountBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the AccountBluprint from the success response
                then send it to the client.
        Args:
            request: AccountValidationRequest
        Result:
            ValidationResult[AccountBlueprint]
        Raises:
            AccountValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationResponseWrapperException.MSG,
                    err_code=AccountValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AccountValidationResponse, result)
        if not response.valid_account:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationResponderException.MSG,
                    err_code=AccountValidationResponderException.ERR_CODE,
                    ex=EmptyAccountCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAccountCarrierException.MSG,
                        err_code=EmptyAccountCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(AccountBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)