# src/exchange/wrapper/validation/struct/node/vector/wrapper.py

"""
Module: exchange.wrapper.validation.struct.node.vector.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import VectorNodeValidationResponse, ValidationResult
from domain import Vector, VectorBlueprint, VectorNode, VectorNodeBlueprint
from err import VectorNodeValidationResponderException, VectorNodeValidationResponseWrapperException, EmptyVectorCarrierException
from exchange import (
    VectorNodeValidationResponder, NodeValidationResponseWrapper, VectorNodeValidationRequest
)
from util import LoggingLevelRouter


class VectorNodeValidationResponseWrapper(
    NodeValidationResponseWrapper[VectorNode]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Vector
                _   VectorBlueprint
            products from VectorNodeValidationResponder.

    Attributes:
        responder: VectorNodeValidationResponder
        
    Provides:
        -   def extract_model(
                    request: VectorNodeValidationRequest
            ) -> ValidationResult[Vector]
            
        -   def extract_blueprint(
                    request: VectorNodeValidationRequest
            ) -> ValidationResult[VectorBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[VectorNodeValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[VectorNodeValidationResponder]
        """
        super().__init__(responder=responder or VectorNodeValidationResponder())
    
    @property
    def responder(self) -> VectorNodeValidationResponder:
        return cast(VectorNodeValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: VectorNodeValidationRequest,
    ) -> ValidationResult[VectorNode]:
        """
        Extract a Vector safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Vector from the success response then send it 
                to the client.
        Args:
            request: VectorNodeValidationRequest
        Result:
            ValidationResult[Vector]
        Raises:
            VectorNodeValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationResponseWrapperException.MSG,
                    err_code=VectorNodeValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorNodeValidationResponse, result)
        if not response.valid_node:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationResponderException.MSG,
                    err_code=VectorNodeValidationResponderException.ERR_CODE,
                    ex=EmptyVectorCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyVectorCarrierException.MSG,
                        err_code=EmptyVectorCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        node = cast(VectorNode, response.valid_node)
        return ValidationResult.success(node)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: VectorNodeValidationRequest,
    ) -> ValidationResult[VectorNodeBlueprint]:
        """
        Extract a VectorBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the VectorBluprint from the success response
                then send it to the client.
        Args:
            request: VectorNodeValidationRequest
        Result:
            ValidationResult[VectorBlueprint]
        Raises:
            VectorNodeValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationResponseWrapperException.MSG,
                    err_code=VectorNodeValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorNodeValidationResponse, result)
        if not response.valid_vector:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationResponderException.MSG,
                    err_code=VectorNodeValidationResponderException.ERR_CODE,
                    ex=EmptyVectorCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyVectorCarrierException.MSG,
                        err_code=EmptyVectorCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(VectorNodeBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)