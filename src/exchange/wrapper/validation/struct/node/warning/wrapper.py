# src/exchange/wrapper/validation/struct/node/warning/wrapper.py

"""
Module: exchange.wrapper.validation.struct.node.warning.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import WarningNodeValidationResponse, ValidationResult
from domain import Warning, WarningBlueprint, EncounterWarningNode, WarningNodeBlueprint
from err import WarningNodeValidationResponderException, WarningNodeValidationResponseWrapperException, EmptyWarningCarrierException
from exchange import (
    WarningNodeValidationResponder, NodeValidationResponseWrapper, EncounterWarningNodeValidationRequest
)
from util import LoggingLevelRouter


class EncounterWarningNodeValidationResponseWrapper(
    NodeValidationResponseWrapper[EncounterWarningNode]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Warning
                _   WarningBlueprint
            products from WarningNodeValidationResponder.

    Attributes:
        responder: WarningNodeValidationResponder
        
    Provides:
        -   def extract_model(
                    request: WarningNodeValidationRequest
            ) -> ValidationResult[Warning]
            
        -   def extract_blueprint(
                    request: WarningNodeValidationRequest
            ) -> ValidationResult[WarningBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[WarningNodeValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[WarningNodeValidationResponder]
        """
        super().__init__(responder=responder or WarningNodeValidationResponder())
    
    @property
    def responder(self) -> WarningNodeValidationResponder:
        return cast(WarningNodeValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: EncounterWarningNodeValidationRequest,
    ) -> ValidationResult[EncounterWarningNode]:
        """
        Extract a Warning safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Warning from the success response then send it 
                to the client.
        Args:
            request: WarningNodeValidationRequest
        Result:
            ValidationResult[Warning]
        Raises:
            WarningNodeValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WarningNodeValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningNodeValidationResponseWrapperException.MSG,
                    err_code=WarningNodeValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(WarningNodeValidationResponse, result)
        if not response.valid_node:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WarningNodeValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningNodeValidationResponderException.MSG,
                    err_code=WarningNodeValidationResponderException.ERR_CODE,
                    ex=EmptyWarningCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyWarningCarrierException.MSG,
                        err_code=EmptyWarningCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        node = cast(EncounterWarningNode, response.valid_node)
        return ValidationResult.success(node)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: EncounterWarningNodeValidationRequest,
    ) -> ValidationResult[WarningNodeBlueprint]:
        """
        Extract a WarningBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the WarningBluprint from the success response
                then send it to the client.
        Args:
            request: WarningNodeValidationRequest
        Result:
            ValidationResult[WarningBlueprint]
        Raises:
            WarningNodeValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WarningNodeValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningNodeValidationResponseWrapperException.MSG,
                    err_code=WarningNodeValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(WarningNodeValidationResponse, result)
        if not response.valid_warning:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WarningNodeValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningNodeValidationResponderException.MSG,
                    err_code=WarningNodeValidationResponderException.ERR_CODE,
                    ex=EmptyWarningCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyWarningCarrierException.MSG,
                        err_code=EmptyWarningCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(WarningNodeBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)