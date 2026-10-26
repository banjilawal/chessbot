# src/exchange/service/validation/model/path/service.py

"""
Module: exchange.service.validation.model.path.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PathValidationResponse, ValidationResult
from domain import Path, PathBlueprint
from err import PathValidationServiceException, PathValidationServiceException, PathCarrierEmptyException
from exchange import (
    PathValidationService, ModelValidationService, PathValidationRequest
)
from util import LoggingLevelRouter


class PathValidationService(
    ModelValidationService[Path]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Path
                _   PathBlueprint
            products from PathValidationService.

    Attributes:
        service: PathValidationService
        
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
            service: Optional[PathValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[PathValidationService]
        """
        super().__init__(service=service or PathValidationService())
    
    @property
    def service(self) -> PathValidationService:
        return cast(PathValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: PathValidationRequest,
    ) -> ValidationResult[Path]:
        """
        Extract a Path safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Path from the success response then send it 
                to the client.
        Args:
            request: PathValidationRequest
        Result:
            ValidationResult[Path]
        Raises:
            PathValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
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
        response = cast(PathValidationResponse, result)
        if not response.valid_model:
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
        model = cast(Path, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: PathValidationRequest,
    ) -> ValidationResult[PathBlueprint]:
        """
        Extract a PathBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the PathBluprint from the success response
                then send it to the client.
        Args:
            request: PathValidationRequest
        Result:
            ValidationResult[PathBlueprint]
        Raises:
            PathValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
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
        response = cast(PathValidationResponse, result)
        if not response.valid_path:
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
        blueprint = cast(PathBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)