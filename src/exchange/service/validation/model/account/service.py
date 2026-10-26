# src/exchange/service/validation/model/account/service.py

"""
Module: exchange.service.validation.model.account.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AccountValidationResponse, ValidationResult
from domain import Account, AccountBlueprint
from err import AccountValidationServiceException, AccountValidationServiceException
from exchange import (
    AccountValidationService, AccountValidationRequest, ModelValidationService
)
from util import LoggingLevelRouter


class AccountValidationService(
    ModelValidationService[Account]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Account
                _   AccountBlueprint
            products from AccountValidationService.

    Attributes:
        service: AccountValidationService
        
    Provides:
        -   def extract_model(
                    request: AccountValidationRequest
            ) -> ValidationResult[Account]
            
        -   def extract_blueprint(
                    request: AccountValidationRequest
            ) -> ValidationResult[AccountBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[AccountValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[AccountValidationService]
        """
        super().__init__(service=service or AccountValidationService())
    
    @property
    def service(self) -> AccountValidationService:
        return cast(AccountValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
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
            AccountValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationServiceException.MSG,
                    err_code=AccountValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AccountValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationServiceException.MSG,
                    err_code=AccountValidationServiceException.ERR_CODE,
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
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the AccountBluprint from the success response
                then send it to the client.
        Args:
            request: AccountValidationRequest
        Result:
            ValidationResult[AccountBlueprint]
        Raises:
            AccountValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationServiceException.MSG,
                    err_code=AccountValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AccountValidationResponse, result)
        if not response.valid_account:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationServiceException.MSG,
                    err_code=AccountValidationServiceException.ERR_CODE,
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