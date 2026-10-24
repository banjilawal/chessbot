# src/exchange/server/validation/model/vector/server.py

"""
Module: exchange.server.validation.model.vector.server
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import VectorValidationResponse, ValidationResult
from domain import Vector, VectorBlueprint
from err import VectorValidationResponderException, VectorValidationServerException, VectorCarrierEmptyException
from exchange import (
    VectorValidationResponder, ModelValidationServer, VectorValidationRequest
)
from util import LoggingLevelRouter


class VectorValidationServer(
    ModelValidationServer[Vector]
):
    """
    Role
        -   Server

    Responsibilities:
        1.  Extract either safe:
                -   Vector
                _   VectorBlueprint
            products from VectorValidationResponder.

    Attributes:
        responder: VectorValidationResponder
        
    Provides:
        -   def extract_model(
                    request: VectorValidationRequest
            ) -> ValidationResult[Vector]
            
        -   def extract_blueprint(
                    request: VectorValidationRequest
            ) -> ValidationResult[VectorBlueprint]

    Super Class:
        ValidationServer
    """
    
    def __init__(
            self,
            responder: Optional[VectorValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[VectorValidationResponder]
        """
        super().__init__(responder=responder or VectorValidationResponder())
    
    @property
    def responder(self) -> VectorValidationResponder:
        return cast(VectorValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: VectorValidationRequest,
    ) -> ValidationResult[Vector]:
        """
        Extract a Vector safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Vector from the success response then send it 
                to the client.
        Args:
            request: VectorValidationRequest
        Result:
            ValidationResult[Vector]
        Raises:
            VectorValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServerException.MSG,
                    err_code=VectorValidationServerException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationResponderException.MSG,
                    err_code=VectorValidationResponderException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Vector, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: VectorValidationRequest,
    ) -> ValidationResult[VectorBlueprint]:
        """
        Extract a VectorBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the VectorBluprint from the success response
                then send it to the client.
        Args:
            request: VectorValidationRequest
        Result:
            ValidationResult[VectorBlueprint]
        Raises:
            VectorValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServerException.MSG,
                    err_code=VectorValidationServerException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorValidationResponse, result)
        if not response.valid_vector:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationResponderException.MSG,
                    err_code=VectorValidationResponderException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(VectorBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)