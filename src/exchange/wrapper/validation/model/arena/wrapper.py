# src/exchange/wrapper/validation/model/arena/wrapper.py

"""
Module: exchange.wrapper.validation.model.arena.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ArenaValidationResponse, ValidationResult
from domain import Arena, ArenaBlueprint
from err import ArenaValidationResponderException, ArenaValidationResponseWrapperException, EmptyArenaCarrierException
from exchange import (
    ArenaValidationResponder, ModelValidationResponseWrapper, ArenaValidationRequest
)
from util import LoggingLevelRouter


class ArenaValidationResponseWrapper(
    ModelValidationResponseWrapper[Arena]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Arena
                _   ArenaBlueprint
            products from ArenaValidationResponder.

    Attributes:
        responder: ArenaValidationResponder
        
    Provides:
        -   def extract_model(
                    request: ArenaValidationRequest
            ) -> ValidationResult[Arena]
            
        -   def extract_blueprint(
                    request: ArenaValidationRequest
            ) -> ValidationResult[ArenaBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[ArenaValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[ArenaValidationResponder]
        """
        super().__init__(responder=responder or ArenaValidationResponder())
    
    @property
    def responder(self) -> ArenaValidationResponder:
        return cast(ArenaValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: ArenaValidationRequest,
    ) -> ValidationResult[Arena]:
        """
        Extract a Arena safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Arena from the success response then send it 
                to the client.
        Args:
            request: ArenaValidationRequest
        Result:
            ValidationResult[Arena]
        Raises:
            ArenaValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationResponseWrapperException.MSG,
                    err_code=ArenaValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ArenaValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationResponderException.MSG,
                    err_code=ArenaValidationResponderException.ERR_CODE,
                    ex=EmptyArenaCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyArenaCarrierException.MSG,
                        err_code=EmptyArenaCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Arena, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ArenaValidationRequest,
    ) -> ValidationResult[ArenaBlueprint]:
        """
        Extract a ArenaBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the ArenaBluprint from the success response
                then send it to the client.
        Args:
            request: ArenaValidationRequest
        Result:
            ValidationResult[ArenaBlueprint]
        Raises:
            ArenaValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationResponseWrapperException.MSG,
                    err_code=ArenaValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ArenaValidationResponse, result)
        if not response.valid_arena:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationResponderException.MSG,
                    err_code=ArenaValidationResponderException.ERR_CODE,
                    ex=EmptyArenaCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyArenaCarrierException.MSG,
                        err_code=EmptyArenaCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ArenaBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)