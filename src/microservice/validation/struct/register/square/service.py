# src/exchange/service/validation/struct/register/square/service.py

"""
Module: exchange.service.validation.struct.register.square.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import SquareRegister, SquareRegisterBlueprint
from err import SquareRegisterCarrierEmptyException, SquareRegisterValidationServiceException
from exchange import SquareRegisterValidationRequest
from microservice import ValidationMicroservice
from transit import SquareRegisterCarrier, SquareRegisterValidationDispatcher
from util import LoggingLevelRouter


class SquareRegisterValidationService(ValidationMicroservice[SquareRegister]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   SquareRegister
                _   SquareRegisterBlueprint
            products from SquareRegisterValidationService.

    Attributes:
        dispatcher: SquareRegisterValidationDispatcher

    Provides:
        -   def extract_model(
                    request: SquareRegisterValidationRequest
            ) -> ValidationResult[SquareRegister]

        -   def extract_blueprint(
                    request: SquareRegisterValidationRequest
            ) -> ValidationResult[SquareRegisterBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[SquareRegisterValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[SquareRegisterValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or SquareRegisterValidationDispatcher())
    
    @property
    def dispatcher(self) -> SquareRegisterValidationDispatcher:
        return cast(SquareRegisterValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: SquareRegisterValidationRequest
    ) -> ValidationResult[SquareRegister]:
        """
        Extract a SquareRegister safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the SquareRegister from the result then send it to the client.
        Args:
            request: SquareRegisterValidationRequest
        Result:
            ValidationResult[SquareRegister]
        Raises:
            SquareRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServiceException.MSG,
                    err_code=SquareRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(SquareRegisterCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServiceException.MSG,
                    err_code=SquareRegisterValidationServiceException.ERR_CODE,
                    ex=SquareRegisterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareRegisterCarrierEmptyException.MSG,
                        err_code=SquareRegisterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(SquareRegister, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: SquareRegisterValidationRequest,
    ) -> ValidationResult[SquareRegisterBlueprint]:
        """
        Extract an SquareRegisterBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the SquareRegisterBlueprint from the result then send it
                to the client.
        Args:
            request: SquareRegisterValidationRequest
        Result:
            ValidationResult[SquareRegisterBlueprint]
        Raises:
            SquareRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServiceException.MSG,
                    err_code=SquareRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(SquareRegisterCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServiceException.MSG,
                    err_code=SquareRegisterValidationServiceException.ERR_CODE,
                    ex=SquareRegisterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareRegisterCarrierEmptyException.MSG,
                        err_code=SquareRegisterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(SquareRegisterBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)