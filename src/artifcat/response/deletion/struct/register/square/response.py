# src/artifact/response/deletion/struct/register/square/response.py

"""
Module: artifact.response.deletion.struct.register.square.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RegisterDeletionResponse, ResponseState, DeletionResult
from exchange import Request, SquareRegisterDeletionRequest
from domain import SquareRegister, SquareRegisterBlueprint
from transit import SquareRegisterCarrier


class SquareRegisterDeletionResponse(
    RegisterDeletionResponse[SquareRegister]
):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a SquareRegister deletion request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: DeletionResult[SquareRegisterCarrier]
        request: SquareRegisterDeletionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Square]
        -   def valid_blueprint() -> Optional[SquareRegisterBlueprint]

        -   def success(
                    request: Request,
                    result: DeletionResult[SquareRegisterCarrier],
            ) -> SquareRegisterDeletionResponse

        -   def failure(
                    request: Request,
                    result: DeletionResult[SquareRegisterCarrier],
                    exception: Exception,
            ) -> SquareRegisterDeletionResponse
            
    Super Class:
        RegisterDeletionResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: SquareRegisterDeletionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult[SquareRegisterCarrier]
            request: SquareRegisterDeletionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> SquareRegisterDeletionRequest:
        return cast(SquareRegisterDeletionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[SquareRegister]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(SquareRegisterCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, SquareRegisterCarrier)
        ):
            return None
        # Handle the case that there is no register in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the register. ---#
        register = cast(SquareRegister, carrier.entity)
        # Handle the case that the register is null or the wrong type.
        if (
                register is None or
                not isinstance(register, SquareRegister)
        ):
            return None
        # Finally send the success result.
        return register
    
    @property
    def valid_blueprint(self) -> Optional[SquareRegisterBlueprint]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(SquareRegisterCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, SquareRegisterCarrier)
        ):
            return None
        # Handle the case that there is no blueprint in the carrier.
        if not carrier.has_blueprint:
            return None
        # --- Extract the blueprint. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null or the wrong type.
        if (
                blueprint is None or
                not isinstance(blueprint, SquareRegisterBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: DeletionResult,
    ) -> SquareRegisterDeletionResponse:
        # Downcast the request into a SquareRegisterDeletionRequest.
        deletion_request = cast(
            SquareRegisterDeletionRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=deletion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: DeletionResult,
            exception: Exception,
    ) -> SquareRegisterDeletionResponse:
        # Downcast the request into a SquareRegisterDeletionRequest.
        deletion_request = cast(
            SquareRegisterDeletionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )