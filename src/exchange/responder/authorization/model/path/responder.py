# src/exchange/responder/authorization/model/path/responder.py

"""
Module: exchange.responder.authorization.model.path.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, PathDecision
from exchange import ModelAuthorizationResponder, PathAuthorizationRequest
from domain import Path
from err import PathAuthorizationResponderException
from transit import PathCarrier, PathAuthorizationDispatcher
from util import LoggingLevelRouter


class PathAuthorizationResponder(ModelAuthorizationResponder[Path]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Path authorization Request-Response workflow.

    Attributes:
        dispatcher: PathAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: PathAuthorizationRequest[T]) -> PathDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PathAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PathAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PathAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> PathAuthorizationDispatcher:
        return cast(PathAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PathAuthorizationRequest
    ) -> PathDecision:
        """
        Certify a candidate is a PathCarrier whose payload is either a Path
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PathAuthorizationRequest
        Result:
            PathDecision
        Raises:
            PathAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PathDecision.failure(
                request=request,
                result=result,
                exception=PathAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathAuthorizationResponderException.MSG,
                    err_code=PathAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PathCarrier, result.payload)
        return PathDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )