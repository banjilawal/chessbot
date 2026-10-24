# src/artifact/response/encounter/kill/response.py

"""
Module: artifact.response.encounter.kill.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class KillEncounterResponse(EncounterResponse[EncounterResult]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Kill's encounter request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: EncounterResult
        request: EncounterRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_kill() -> Optional[T]
        -   def valid_blueprint() -> Optional[KillBlueprint[T]]

        -   def success(
                    request: Request,
                    result: EncounterResult[T],
            ) -> EncounterResponse[T]

        -   def failure(
                    request: Request,
                    result: EncounterResult[T],
                    exception: Exception,
            ) -> EncounterResponse[T]

    Super Class:
        EncounterResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: EncounterResult,
            request: KillEncounterRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: EncounterResult,
            request: KillEncounterRequest[T],
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> EncounterResult:
        return cast(EncounterResult, super().result)
        
    @property
    def request(self) -> KillEncounterRequest[T]:
        return cast(KillEncounterRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_kill(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[KillBlueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: EncounterResult,
    ) -> KillEncounterResponse:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            KillEncounterRequest[T],
            request
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=encounter_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: EncounterResult,
            exception: Exception,
    ) -> KillEncounterResponse:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            KillEncounterRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=encounter_request,
            state=ResponseState.FAILURE,
        )
