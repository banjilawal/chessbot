# src/exchange/service/validation/context/account/service.py

"""
Module: exchange.service.validation.context.account.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import AccountContext, AccountContextBlueprint
from exchange import AccountContextValidationRequest
from microservice import ValidationMicroservice
from transit import AccountContextCarrier, AccountContextValidationDispatcher
from util import LoggingLevelRouter


class AccountContextValidationService(ValidationMicroservice[AccountContext]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   AccountContext
                _   AccountContextBlueprint
            products from AccountContextValidationService.

    Attributes:
        dispatcher: AccountContextValidationDispatcher

    Provides:
        -   def extract_model(
                    request: AccountContextValidationRequest
            ) -> ValidationResult[AccountContext]

        -   def extract_blueprint(
                    request: AccountContextValidationRequest
            ) -> ValidationResult[AccountContextBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[AccountContextValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AccountContextValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AccountContextValidationDispatcher())
    
    @property
    def dispatcher(self) -> AccountContextValidationDispatcher:
        return cast(AccountContextValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: AccountContextValidationRequest
    ) -> ValidationResult[AccountContext]:
        """
        Extract an AccountContext safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the AccountContext from the result then send it to the client.
        Args:
            request: AccountContextValidationRequest
        Result:
            ValidationResult[AccountContext]
        Raises:
            AccountContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(AccountContextCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationServiceException.MSG,
                    err_code=AccountContextValidationServiceException.ERR_CODE,
                    ex=AccountContextCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCarrierEmptyException.MSG,
                        err_code=AccountContextCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(AccountContext, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AccountContextValidationRequest,
    ) -> ValidationResult[AccountContextBlueprint]:
        """
        Extract an AccountContextBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the AccountContextBlueprint from the result then send it
                to the client.
        Args:
            request: AccountContextValidationRequest
        Result:
            ValidationResult[AccountContextBlueprint]
        Raises:
            AccountContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(AccountContextCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationServiceException.MSG,
                    err_code=AccountContextValidationServiceException.ERR_CODE,
                    ex=AccountContextCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountContextCarrierEmptyException.MSG,
                        err_code=AccountContextCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(AccountContextBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)