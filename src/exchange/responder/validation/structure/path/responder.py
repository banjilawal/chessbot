# src/exchange/responder/validation/structure/path/exchange.py

"""
Module: exchange.responder.validation.structure.path.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, PathValidationResponse
from exchange import StructureValidationResponder, PathValidationRequest
from domain import Path
from err import PathValidationResponderException
from transit import PathCarrier, PathValidationDispatcher
from util import LoggingLevelRouter


class PathValidationResponder(StructureValidationResponder[Path]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Path validation Request-Response workflow.

    Attributes:
        dispatcher: PathValidationDispatcher[T]

    Provides:
        -   def submit(request: PathValidationRequest[T]) -> PathValidationResponse[T]

    Super Class:
        StructureValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PathValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PathValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PathValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> PathValidationDispatcher:
        return cast(PathValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PathValidationRequest
    ) -> PathValidationResponse:
        """
        Certify a candidate is a PathCarrier whose payload is either a Path
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PathValidationRequest
        Result:
            PathValidationResponse
        Raises:
            PathValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PathValidationResponse.failure(
                request=request,
                result=result,
                exception=PathValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationResponderException.MSG,
                    err_code=PathValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PathCarrier, result.payload)
        return PathValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )