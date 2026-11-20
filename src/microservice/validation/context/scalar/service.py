# src/exchange/service/validation/context/scalar/service.py

"""
Module: exchange.service.validation.context.scalar.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ScalarValidationResponse, ValidationResult
from domain import Scalar, ScalarBlueprint
from err import ScalarContextValidationServiceException, ScalarContextValidationServiceException, ScalarCarrierEmptyException
from exchange import (
    ScalarContextValidationService, ContextValidationService, ScalarValidationRequest
)
from util import LoggingLevelRouter


class ScalarContextValidationService(
    ContextValidationService[Scalar]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Scalar
                _   ScalarBlueprint
            products from ScalarContextValidationService.

    Attributes:
        dispatcher: ScalarContextValidationDispatcher
        
    Provides:
        -   def extract_context(
                    request: ScalarValidationRequest
            ) -> ValidationResult[Scalar]
            
        -   def extract_blueprint(
                    request: ScalarValidationRequest
            ) -> ValidationResult[ScalarBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[ScalarContextValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ScalarContextValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or ScalarContextValidationDispatcher())
    
    @property
    def dispatcher(self) -> ScalarContextValidationDispatcher:
        return cast(ScalarContextValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: ScalarValidationRequest,
    ) -> ValidationResult[Scalar]:
        """
        Extract a Scalar safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Scalar from the success response then send it 
                to the client.
        Args:
            request: ScalarValidationRequest
        Result:
            ValidationResult[Scalar]
        Raises:
            ScalarContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.dispatcher.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarContextValidationServiceException.MSG,
                    err_code=ScalarContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        carrier = cast(ScalarValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarContextValidationServiceException.MSG,
                    err_code=ScalarContextValidationServiceException.ERR_CODE,
                    ex=ScalarCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ScalarCarrierEmptyException.MSG,
                        err_code=ScalarCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Scalar, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ScalarValidationRequest,
    ) -> ValidationResult[ScalarBlueprint]:
        """
        Extract a ScalarBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the ScalarBluprint from the success response
                then send it to the client.
        Args:
            request: ScalarValidationRequest
        Result:
            ValidationResult[ScalarBlueprint]
        Raises:
            ScalarContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.dispatcher.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarContextValidationServiceException.MSG,
                    err_code=ScalarContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        carrier = cast(ScalarValidationResponse, result)
        if not response.valid_scalar:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarContextValidationServiceException.MSG,
                    err_code=ScalarContextValidationServiceException.ERR_CODE,
                    ex=ScalarCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ScalarCarrierEmptyException.MSG,
                        err_code=ScalarCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ScalarBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)