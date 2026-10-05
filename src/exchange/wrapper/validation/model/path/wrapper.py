# src/exchange/wrapper/validation/model/path/wrapper.py

"""
Module: exchange.wrapper.validation.model.path.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PathValidationResponse, ValidationResult
from domain import Path, PathBlueprint
from err import PathValidationResponderException, PathValidationResponseWrapperException, PathCarrierEmptyException
from exchange import (
    PathValidationResponder, ModelValidationResponseWrapper, PathValidationRequest
)
from util import LoggingLevelRouter


class PathValidationResponseWrapper(
    ModelValidationResponseWrapper[Path]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Path
                _   PathBlueprint
            products from PathValidationResponder.

    Attributes:
        responder: PathValidationResponder
        
    Provides:
        -   def extract_model(
                    request: PathValidationRequest
            ) -> ValidationResult[Path]
            
        -   def extract_blueprint(
                    request: PathValidationRequest
            ) -> ValidationResult[PathBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[PathValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[PathValidationResponder]
        """
        super().__init__(responder=responder or PathValidationResponder())
    
    @property
    def responder(self) -> PathValidationResponder:
        return cast(PathValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: PathValidationRequest,
    ) -> ValidationResult[Path]:
        """
        Extract a Path safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Path from the success response then send it 
                to the client.
        Args:
            request: PathValidationRequest
        Result:
            ValidationResult[Path]
        Raises:
            PathValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationResponseWrapperException.MSG,
                    err_code=PathValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PathValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationResponderException.MSG,
                    err_code=PathValidationResponderException.ERR_CODE,
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
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the PathBluprint from the success response
                then send it to the client.
        Args:
            request: PathValidationRequest
        Result:
            ValidationResult[PathBlueprint]
        Raises:
            PathValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationResponseWrapperException.MSG,
                    err_code=PathValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PathValidationResponse, result)
        if not response.valid_path:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationResponderException.MSG,
                    err_code=PathValidationResponderException.ERR_CODE,
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