# src/exchange/service/validation/context/account/service.py

"""
Module: exchange.service.validation.context.account.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AccountContextValidationResponse, AccountValidationResponse, ValidationResponse
from domain import AccountContext, AccountContextBlueprint
from exchange import (
    AccountContextValidationRequest, AccountContextValidationResponder, AccountValidationRequest,
    ContextValidationService
)

from util import LoggingLevelRouter


class AccountContextValidationService(
    ContextValidationService[AccountContext]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Account
                _   AccountBlueprint
            products from AccountContextValidationService.

    Attributes:
        responder: AccountContextValidationResponder
        
    Provides:
        -   def extract_context(
                    request: AccountValidationRequest
            ) -> ValidationResponse[Account]
            
        -   def extract_blueprint(
                    request: AccountValidationRequest
            ) -> ValidationResponse[AccountBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            responder: Optional[AccountContextValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[AccountContextValidationResponder]
        """
        super().__init__(responder=responder or AccountContextValidationResponder())

    @property
    def responder(self) -> AccountContextValidationResponder:
        return cast(AccountContextValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: AccountContextValidationRequest,
    ) -> ValidationResponse[AccountContext]:
        """
        Extract a Account safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the service
                fails.
            2.  Otherwise, extract the Account from the success response then send it 
                to the client.
        Args:
            request: AccountValidationRequest
        Response:
            ValidationResponse[Account]
        Raises:
            AccountContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        response = self.responder.execute(request)
        if response.is_failure:
            # Send the exception chain on failure.
            return ValidationResponse.failure(
                AccountContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationServiceException.MSG,
                    err_code=AccountContextValidationServiceException.ERR_CODE,
                    ex=response.exception,
                )
            )
        if response.valid_model is None:
            # Send the exception chain on failure.
            return ValidationResponse.failure(
                AccountContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationServiceException.MSG,
                    err_code=AccountContextValidationServiceException.ERR_CODE,
                    ex=EmptyAccountContextCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAccountContextCarrierException.MSG,
                        err_code=EmptyAccountContextCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(AccountContext, response.valid_model)
        return ValidationResponse.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AccountContextValidationRequest,
    ) -> ValidationResponse[AccountContextBlueprint]:
        """
        Extract an AccountContextBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the service
                fails.
            2.  Otherwise, extract the AccountBluprint from the success response
                then send it to the client.
        Args:
            request: AccountValidationRequest
        Response:
            ValidationResponse[AccountBlueprint]
        Raises:
            AccountContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        response = self.responder.execute(request)
        if response.is_failure:
            # Send the exception chain on failure.
            return ValidationResponse.failure(
                exception=AccountContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationServiceException.MSG,
                    err_code=AccountContextValidationServiceException.ERR_CODE,
                    ex=response.exception,
                )
            )
        if response.valid_blueprint is None:
            # Send the exception chain on failure.
            return ValidationResponse.failure(
                AccountContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationServiceException.MSG,
                    err_code=AccountContextValidationServiceException.ERR_CODE,
                    ex=EmptyAccountCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAccountCarrierException.MSG,
                        err_code=EmptyAccountCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(AccountContextBlueprint, response.valid_blueprint)
        return ValidationResponse.success(blueprint)