# src/exchange/responder/fabrication/model/path/responder.py

"""
Module: exchange.responder.fabrication.model.path.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, PathBuildResponse
from exchange import ModelBuildResponder, PathBuildRequest
from domain import Path
from err import PathBuildResponderException
from transit import PathCarrier, PathBuildDispatcher
from util import LoggingLevelRouter


class PathBuildResponder(ModelBuildResponder[Path]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Path build Request-Response workflow.

    Attributes:
        dispatcher: PathBuildDispatcher[T]

    Provides:
        -   def submit(request: PathBuildRequest[T]) -> PathBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PathBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PathBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PathBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> PathBuildDispatcher:
        return cast(PathBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PathBuildRequest
    ) -> PathBuildResponse:
        """
        Certify a candidate is a PathCarrier whose payload is either a Path
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PathBuildRequest
        Result:
            PathBuildResponse
        Raises:
            PathValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PathBuildResponse.failure(
                request=request,
                result=result,
                exception=PathBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathBuildResponderException.MSG,
                    err_code=PathBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PathCarrier, result.payload)
        return PathBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )