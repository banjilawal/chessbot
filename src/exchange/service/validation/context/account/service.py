# src/exchange/service/validation/context/account/service.py

"""
Module: exchange.service.validation.context.account.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AccountValidationResponse, ValidationResult
from domain import Account, AccountBlueprint
from err import AccountContextValidationServiceException, AccountContextValidationServiceException
from exchange import (
    AccountContextValidationService, AccountValidationRequest, ContextValidationService
)
from util import LoggingLevelRouter


class AccountContextValidationService(
    ContextValidationService[Account]
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
        service: AccountContextValidationService
        
    Provides:
        -   def extract_context(
                    request: AccountValidationRequest
            ) -> ValidationResult[Account]
            
        -   def extract_blueprint(
                    request: AccountValidationRequest
            ) -> ValidationResult[AccountBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[AccountContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[AccountContextValidationService]
        """
        super().__init__(service=service or AccountContextValidationService())
    
    @property
    def service(self) -> AccountContextValidationService:
        return cast(AccountContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: AccountValidationRequest,
    ) -> ValidationResult[Account]:
        """
        Extract a Account safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Account from the success response then send it 
                to the client.
        Args:
            request: AccountValidationRequest
        Result:
            ValidationResult[Account]
        Raises:
            AccountContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationServiceException.MSG,
                    err_code=AccountContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AccountValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
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
        context = cast(Account, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AccountValidationRequest,
    ) -> ValidationResult[AccountBlueprint]:
        """
        Extract a AccountBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the AccountBluprint from the success response
                then send it to the client.
        Args:
            request: AccountValidationRequest
        Result:
            ValidationResult[AccountBlueprint]
        Raises:
            AccountContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationServiceException.MSG,
                    err_code=AccountContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AccountValidationResponse, result)
        if not response.valid_account:
            # Send the exception chain on failure.
            return ValidationResult.failure(
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
        blueprint = cast(AccountBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)