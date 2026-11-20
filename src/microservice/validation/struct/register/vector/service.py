# src/exchange/service/validation/struct/register/vector/service.py

"""
Module: exchange.service.validation.struct.register.vector.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import VectorRegister, VectorRegisterBlueprint
from err import VectorRegisterValidationServiceException
from exchange import VectorRegisterValidationRequest
from microservice import ValidationMicroservice
from transit import VectorRegisterCarrier, VectorRegisterValidationDispatcher
from util import LoggingLevelRouter


class VectorRegisterValidationService(ValidationMicroservice[VectorRegister]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   VectorRegister
                _   VectorRegisterBlueprint
            products from VectorRegisterValidationService.

    Attributes:
        dispatcher: VectorRegisterValidationDispatcher

    Provides:
        -   def extract_model(
                    request: VectorRegisterValidationRequest
            ) -> ValidationResult[VectorRegister]

        -   def extract_blueprint(
                    request: VectorRegisterValidationRequest
            ) -> ValidationResult[VectorRegisterBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[VectorRegisterValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorRegisterValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or VectorRegisterValidationDispatcher())
    
    @property
    def dispatcher(self) -> VectorRegisterValidationDispatcher:
        return cast(VectorRegisterValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: VectorRegisterValidationRequest
    ) -> ValidationResult[VectorRegister]:
        """
        Extract a VectorRegister safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the VectorRegister from the result then send it to the client.
        Args:
            request: VectorRegisterValidationRequest
        Result:
            ValidationResult[VectorRegister]
        Raises:
            VectorRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationServiceException.MSG,
                    err_code=VectorRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(VectorRegisterCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationServiceException.MSG,
                    err_code=VectorRegisterValidationServiceException.ERR_CODE,
                    ex=VectorRegisterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorRegisterCarrierEmptyException.MSG,
                        err_code=VectorRegisterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(VectorRegister, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: VectorRegisterValidationRequest,
    ) -> ValidationResult[VectorRegisterBlueprint]:
        """
        Extract an VectorRegisterBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the VectorRegisterBlueprint from the result then send it
                to the client.
        Args:
            request: VectorRegisterValidationRequest
        Result:
            ValidationResult[VectorRegisterBlueprint]
        Raises:
            VectorRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationServiceException.MSG,
                    err_code=VectorRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(VectorRegisterCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationServiceException.MSG,
                    err_code=VectorRegisterValidationServiceException.ERR_CODE,
                    ex=VectorRegisterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorRegisterCarrierEmptyException.MSG,
                        err_code=VectorRegisterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(VectorRegisterBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)