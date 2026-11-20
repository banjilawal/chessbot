# src/exchange/service/validation/struct/register/coord/service.py

"""
Module: exchange.service.validation.struct.register.coord.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import CoordRegister, CoordRegisterBlueprint
from err import CoordRegisterCarrierEmptyException, CoordRegisterValidationServiceException
from exchange import CoordRegisterValidationRequest
from microservice import ValidationMicroservice
from transit import CoordRegisterCarrier, CoordRegisterValidationDispatcher
from util import LoggingLevelRouter


class CoordRegisterValidationService(ValidationMicroservice[CoordRegister]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   CoordRegister
                _   CoordRegisterBlueprint
            products from CoordRegisterValidationService.

    Attributes:
        dispatcher: CoordRegisterValidationDispatcher

    Provides:
        -   def extract_model(
                    request: CoordRegisterValidationRequest
            ) -> ValidationResult[CoordRegister]

        -   def extract_blueprint(
                    request: CoordRegisterValidationRequest
            ) -> ValidationResult[CoordRegisterBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[CoordRegisterValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordRegisterValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or CoordRegisterValidationDispatcher())
    
    @property
    def dispatcher(self) -> CoordRegisterValidationDispatcher:
        return cast(CoordRegisterValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: CoordRegisterValidationRequest
    ) -> ValidationResult[CoordRegister]:
        """
        Extract a CoordRegister safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the CoordRegister from the result then send it to the client.
        Args:
            request: CoordRegisterValidationRequest
        Result:
            ValidationResult[CoordRegister]
        Raises:
            CoordRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationServiceException.MSG,
                    err_code=CoordRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(CoordRegisterCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationServiceException.MSG,
                    err_code=CoordRegisterValidationServiceException.ERR_CODE,
                    ex=CoordRegisterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordRegisterCarrierEmptyException.MSG,
                        err_code=CoordRegisterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(CoordRegister, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: CoordRegisterValidationRequest,
    ) -> ValidationResult[CoordRegisterBlueprint]:
        """
        Extract an CoordRegisterBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the CoordRegisterBlueprint from the result then send it
                to the client.
        Args:
            request: CoordRegisterValidationRequest
        Result:
            ValidationResult[CoordRegisterBlueprint]
        Raises:
            CoordRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationServiceException.MSG,
                    err_code=CoordRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(CoordRegisterCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationServiceException.MSG,
                    err_code=CoordRegisterValidationServiceException.ERR_CODE,
                    ex=CoordRegisterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordRegisterCarrierEmptyException.MSG,
                        err_code=CoordRegisterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(CoordRegisterBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)