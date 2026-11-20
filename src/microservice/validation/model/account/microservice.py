# src/exchange/service/validation/model/account/service.py

"""
Module: exchange.service.validation.model.account.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Account, AccountBlueprint
from err import AccountCarrierEmptyException, AccountValidationServiceException
from exchange import AccountValidationRequest
from microservice import ValidationMicroservice
from transit import AccountCarrier, AccountValidationDispatcher
from util import LoggingLevelRouter


class AccountValidationService(ValidationMicroservice[Account]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Account
                _   AccountBlueprint
            products from AccountValidationService.

    Attributes:
        dispatcher: AccountValidationDispatcher
        
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
            dispatcher: Optional[AccountValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AccountValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AccountValidationDispatcher())
    
    @property
    def dispatcher(self) -> AccountValidationDispatcher:
        return cast(AccountValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: AccountValidationRequest) -> ValidationResult[Account]:
        """
        Extract an Account safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Account from the result then send it to the client.
        Args:
            request: AccountValidationRequest
        Result:
            ValidationResult[Account]
        Raises:
            AccountValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(AccountCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationServiceException.MSG,
                    err_code=AccountValidationServiceException.ERR_CODE,
                    ex=AccountCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCarrierEmptyException.MSG,
                        err_code=AccountCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Account, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AccountValidationRequest,
    ) -> ValidationResult[AccountBlueprint]:
        """
        Extract an AccountBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the AccountBlueprint from the result then send it
                to the client.
        Args:
            request: AccountValidationRequest
        Result:
            ValidationResult[AccountBlueprint]
        Raises:
            AccountValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(AccountCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationServiceException.MSG,
                    err_code=AccountValidationServiceException.ERR_CODE,
                    ex=AccountCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCarrierEmptyException.MSG,
                        err_code=AccountCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(AccountBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)