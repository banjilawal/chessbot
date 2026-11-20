# src/exchange/service/validation/model/vector/service.py

"""
Module: exchange.service.validation.model.vector.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Vector, VectorBlueprint
from err import VectorCarrierEmptyException, VectorValidationServiceException
from exchange import VectorValidationRequest
from microservice import ValidationMicroservice
from transit import VectorCarrier, VectorValidationDispatcher
from util import LoggingLevelRouter


class VectorValidationService(ValidationMicroservice[Vector]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Vector
                _   VectorBlueprint
            products from VectorValidationService.

    Attributes:
        dispatcher: VectorValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: VectorValidationRequest
            ) -> ValidationResult[Vector]
            
        -   def extract_blueprint(
                    request: VectorValidationRequest
            ) -> ValidationResult[VectorBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[VectorValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or VectorValidationDispatcher())
    
    @property
    def dispatcher(self) -> VectorValidationDispatcher:
        return cast(VectorValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: VectorValidationRequest) -> ValidationResult[Vector]:
        """
        Extract an Vector safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Vector from the result then send it to the client.
        Args:
            request: VectorValidationRequest
        Result:
            ValidationResult[Vector]
        Raises:
            VectorValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServiceException.MSG,
                    err_code=VectorValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(VectorCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServiceException.MSG,
                    err_code=VectorValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Vector, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: VectorValidationRequest,
    ) -> ValidationResult[VectorBlueprint]:
        """
        Extract an VectorBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the VectorBlueprint from the result then send it
                to the client.
        Args:
            request: VectorValidationRequest
        Result:
            ValidationResult[VectorBlueprint]
        Raises:
            VectorValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServiceException.MSG,
                    err_code=VectorValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(VectorCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServiceException.MSG,
                    err_code=VectorValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(VectorBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)