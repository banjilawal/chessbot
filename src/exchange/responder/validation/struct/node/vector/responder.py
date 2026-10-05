# src/exchange/responder/validation/struct/node/vector/responder.py

"""
Module: exchange.responder.validation.struct.node.vector.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, VectorNodeValidationResponse
from domain import VectorNode
from exchange import NodeValidationResponder, VectorNodeValidationRequest
from err import VectorNodeValidationResponderException
from transit import VectorCarrier, VectorNodeCarrier, VectorNodeValidationDispatcher
from util import LoggingLevelRouter


class VectorNodeValidationResponder(NodeValidationResponder[VectorNode]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the VectorNode validation Request-Response workflow.

    Attributes:
        dispatcher: VectorNodeValidationDispatcher[T]

    Provides:
        -   def submit(request: VectorNodeValidationRequest[T]) -> VectorNodeValidationResponse[T]

    Super Class:
        NodeValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorNodeValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorNodeValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorNodeValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorNodeValidationDispatcher:
        return cast(VectorNodeValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorNodeValidationRequest
    ) -> VectorNodeValidationResponse:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorNodeValidationRequest
        Result:
            VectorNodeValidationResponse
        Raises:
            VectorValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorNodeValidationResponse.failure(
                request=request,
                result=result,
                exception=VectorNodeValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationResponderException.MSG,
                    err_code=VectorNodeValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorNodeCarrier, result.payload)
        return VectorNodeValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )