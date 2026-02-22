# src/chess/square/database/core/util/occupation/token/service.py

"""
Module: chess.square.database.core.util.occupation.token.service
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import List

from chess.square import (
    AddingSquareOccupantException, RemovingSquareOccupantException, RosterFormationCoordinator, Square,
    SquareNotFoundException, SquareService, OccupationServiceException
)
from chess.system import DeletionResult, IdFactory, LoggingLevelRouter, UpdateResult
from chess.token import Token, TokenService


class OccupationService:
    SERVICE_NAME = "OccupationService"
    _id: int
    _name: str
    _formation_coordinator: RosterFormationCoordinator
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="OccupationService"),
            formation_coordinator: RosterFormationCoordinator = RosterFormationCoordinator()
    ):
        self._id = id
        self._name = name
        self._formation_coordinator = formation_coordinator
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def formation_coordinator(self) -> RosterFormationCoordinator:
        return self._formation_coordinator
    
    @LoggingLevelRouter.monitor
    def add_occupant_to_square(
            self,
            token: Token,
            square: Square,
            square_list: list[Square],
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
    ) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  If token_service cannot verify the occupation candidate is actionable send the wrapped exception
                in the InsertionResult.
            2.  If the square either:
                    *   Fails validation.
                    *   Searching for it in the database raises an error.
                    *   The square is not in the database.
                send the wrapped exception in the InsertionResult.
            3.  If the occupation fails send the wrapped exception in the InsertionResult.
            4.  Add an entry for the occupant in the token_map then send the success InsertionResult.
        # PARAMETERS:
            *   token (Token)
            *   square (Square)
            *   token_service (TokenService)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On occupant not found: Empty DeletionResult.
        # RAISES:
            *   SquareDatabaseException
            *   SquareToOccupyNotFoundException
            *   AddingSquareOccupantException
        """
        method = "SquareDatabase.add_occupant_to_square"
        
        # Handle the case that, the square is not certified safe.
        square_validation = square_service.validator.validate(square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=OccupationServiceException(
                    message=f"ServiceId:{self._id}, {method}: {OccupationServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # --- After the square is validated, get a snapshot of its pre-update state. ---#
        pre_update_square = deepcopy(square)
        
        # Handle the case that the token is not active
        actionable_token_validation = token_service.verify_access_token(token)
        if actionable_token_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=OccupationServiceException(
                    message=f"ServiceId:{self._id}, {method}: {OccupationServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=actionable_token_validation.exception
                    )
                )
            )
        # Handle the case that the target square is not in the list
        if square not in square_list:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=OccupationServiceException(
                    message=f"ServiceId:{self._id}, {method}: {OccupationServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=SquareNotFoundException(f"{method}: {SquareNotFoundException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # Handle the case that the occupation fails.
        insertion_result = square_service.add_occupant_to_square(square, token)
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=OccupationServiceException(
                    message=f"ServiceId:{self._id}, {method}: {OccupationServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        
        # --- Send the success result to the client. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=square)
    
    @LoggingLevelRouter.monitor
    def delete_occupant_by_search(
            self,
            occupant: Token,
            square_list: List[Square],
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the search handler cannot certify the occupant is a valid token the exception chain will include.
                TokenVerificationFailedException.
            2.  If the token is not found in any of the squares send a nothing_to_delete result.
            3.  If the token was found in a square but the removal failed send the wrapped exception in the
                DeletionResult.
            4.  When the token is successfully removed from the square remove its entry from the token_map then
                send the ejected token in the DeletionResult.
        # PARAMETERS:
            *   occupant (Token)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On occupant not found: Empty DeletionResult.
        # RAISES:
            *   SquareDatabaseException
            *   DeleteTokenBySearchException
        """
        method = "SquareService.empty_square_by_token_search"
        
        # Handle the case that the token is not certified as safe.
        token_validation = token_service.validator.validate(occupant)
        if token_validation.is_failure:
            # Send the debug exception to the client.
            return DeletionResult.failure(
                exception=OccupationServiceException(
                    message=f"ServiceId:{self._id}, {method}: {OccupationServiceException.ERROR_CODE}",
                    ex=RemovingSquareOccupantException(
                        message=f"{method}: {RemovingSquareOccupantException.ERROR_CODE}",
                        ex=token_validation.exception
                    )
                )
            )
        
        # --- Find the square holding the token ---#
        occupations = [square for square in square_list if square.occupant == occupant]
        
        # Process the simplest case: No squares are holding the token.
        if len(occupations) == 0:
            return DeletionResult.nothing_to_delete()
        # Process the case: Some squares are holding the token
        return self._eviction_handler(occupations, square_service)
    
    def _eviction_handler(
            self,
            occupied_squares: List[Square],
            square_service: SquareService = SquareService()
    ) -> DeletionResult[Token]:
        """
        """
        method = "SquareService._eviction_handler"
        
        # --- Expecting only one square in the list.  ---#
        occupant: Token = None
        for square in occupied_squares:
            # --- Handoff the deletion responsibility to square_service. ---#
            deletion_result = square_service.remove_occupant(square)
            
            # Handle the case that, the removal is not completed.
            if deletion_result.is_failure:
                # Send the debug exception to the client.
                return DeletionResult.failure(
                    exception=OccupationServiceException(
                        message=f"ServiceId:{self._id}, {method}: {OccupationServiceException.ERROR_CODE}",
                        ex=deletion_result.exception
                    )
                )
            occupant = deletion_result.payload
        # --- After the loop completes return the success result to the client. ---#
        return DeletionResult.success(payload=occupant)
        