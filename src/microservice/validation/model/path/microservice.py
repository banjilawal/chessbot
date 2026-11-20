# src/exchange/service/validation/model/path/service.py

"""
Module: exchange.service.validation.model.path.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Path, PathBlueprint
from err import PathCarrierEmptyException, PathValidationServiceException
from exchange import PathValidationRequest
from microservice import ValidationMicroservice
from transit import PathCarrier, PathValidationDispatcher
from util import LoggingLevelRouter


class PathValidationService(ValidationMicroservice[Path]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Path
                _   PathBlueprint
            products from PathValidationService.

    Attributes:
        dispatcher: PathValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: PathValidationRequest
            ) -> ValidationResult[Path]
            
        -   def extract_blueprint(
                    request: PathValidationRequest
            ) -> ValidationResult[PathBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[PathValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PathValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or PathValidationDispatcher())
    
    @property
    def dispatcher(self) -> PathValidationDispatcher:
        return cast(PathValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: PathValidationRequest) -> ValidationResult[Path]:
        """
        Extract an Path safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Path from the result then send it to the client.
        Args:
            request: PathValidationRequest
        Result:
            ValidationResult[Path]
        Raises:
            PathValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationServiceException.MSG,
                    err_code=PathValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(PathCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationServiceException.MSG,
                    err_code=PathValidationServiceException.ERR_CODE,
                    ex=PathCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathCarrierEmptyException.MSG,
                        err_code=PathCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Path, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: PathValidationRequest,
    ) -> ValidationResult[PathBlueprint]:
        """
        Extract an PathBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the PathBlueprint from the result then send it
                to the client.
        Args:
            request: PathValidationRequest
        Result:
            ValidationResult[PathBlueprint]
        Raises:
            PathValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationServiceException.MSG,
                    err_code=PathValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(PathCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationServiceException.MSG,
                    err_code=PathValidationServiceException.ERR_CODE,
                    ex=PathCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathCarrierEmptyException.MSG,
                        err_code=PathCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(PathBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)