# src/exchange/service/validation/context/path/service.py

"""
Module: exchange.service.validation.context.path.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PathValidationResponse, ValidationResult
from domain import Path, PathBlueprint
from err import PathContextValidationServiceException, PathContextValidationServiceException, PathCarrierEmptyException
from exchange import (
    PathContextValidationService, ContextValidationService, PathValidationRequest
)
from util import LoggingLevelRouter


class PathContextValidationService(
    ContextValidationService[Path]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Path
                _   PathBlueprint
            products from PathContextValidationService.

    Attributes:
        service: PathContextValidationService
        
    Provides:
        -   def extract_context(
                    request: PathValidationRequest
            ) -> ValidationResult[Path]
            
        -   def extract_blueprint(
                    request: PathValidationRequest
            ) -> ValidationResult[PathBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[PathContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[PathContextValidationService]
        """
        super().__init__(service=service or PathContextValidationService())
    
    @property
    def service(self) -> PathContextValidationService:
        return cast(PathContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
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
            PathContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathContextValidationServiceException.MSG,
                    err_code=PathContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PathValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathContextValidationServiceException.MSG,
                    err_code=PathContextValidationServiceException.ERR_CODE,
                    ex=PathCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathCarrierEmptyException.MSG,
                        err_code=PathCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Path, response.valid_context)
        return ValidationResult.success(context)
    
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
            PathContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathContextValidationServiceException.MSG,
                    err_code=PathContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PathValidationResponse, result)
        if not response.valid_path:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathContextValidationServiceException.MSG,
                    err_code=PathContextValidationServiceException.ERR_CODE,
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