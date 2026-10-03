# src/exchange/responder/validation/model/team/exchange.py

"""
Module: exchange.responder.validation.model.team.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, TeamValidationResponse
from err import TeamValidationResponderException
from exchange import ModelValidationResponder, TeamValidationRequest
from domain import Team
from transit import TeamCarrier, TeamValidationDispatcher
from util import LoggingLevelRouter


class TeamValidationResponder(ModelValidationResponder[Team]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Team validation Request-Response workflow.

    Attributes:
        dispatcher: TeamValidationDispatcher[T]

    Provides:
        -   def submit(request: TeamValidationRequest[T]) -> TeamValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TeamValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TeamValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TeamValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> TeamValidationDispatcher:
        return cast(TeamValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TeamValidationRequest
    ) -> TeamValidationResponse:
        """
        Certify a candidate is a TeamCarrier whose payload is either a Team
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TeamValidationRequest
        Result:
            TeamValidationResponse
        Raises:
            TeamValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TeamValidationResponse.failure(
                request=request,
                result=result,
                exception=TeamValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationResponderException.MSG,
                    err_code=TeamValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TeamCarrier, result.payload)
        return TeamValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )