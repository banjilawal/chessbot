# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import cast

from chess.square.service.exception.insertion import TargetSquareNotEmptyException
from chess.square.state import SquareState
from chess.system import EntityService, InsertionResult, LoggingLevelRouter, id_emitter
from chess.square import (
    AddingFormationToSquareFailedException, Square, SquareBuilder, SquareServiceException,
    SquareValidator
)
from chess.team import Team, TeamService
from chess.token import Token, TokenBoardState, TokenContext, TokenService


class SquareService(EntityService[Square]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Square microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   SquareService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "SquareService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: SquareBuilder = SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (SquareFactory)
            *   validator (SquareValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> SquareBuilder:
        """get SquareBuilder"""
        return cast(SquareBuilder, self.entity_builder)
    
    @property
    def validator(self) -> SquareValidator:
        """get SquareValidator"""
        return cast(SquareValidator, self.entity_validator)
    
    @LoggingLevelRouter.monitor
    def accept_from_tea_roster(
            self,
            square: Square,
            team: Team,
            team_service: TeamService = TeamService()
    ) -> InsertionResult[Token]:
        method = "squareService.acceptFromTeaRoster"
        
        # Handle the case that the square is not certified safe.
        square_validation = self.validator.validate(candidate=square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # Handle the case that the token is not certified safe.
        team_validation = team_service.validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=team_validation.exception
                    )
                )
            )
        # Handle the case that the squre is not empty
        if square.state != SquareState.EMPTY:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=TargetSquareNotEmptyException(f"{method}: {TargetSquareNotEmptyException.DEFAULT_MESSAGE}")
                    )
                )
            )
        search_result = team_service.roster.search_for_token(context=TokenContext(opening_square=square))
        
        #
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=search_result.exception.exception
                    )
                )
            )
        if search_result.is_empty:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        token = cast(Token, search_result.payload[0])
        
        if token.board_state != TokenBoardState.NEVER_BEEN_PLACED:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        deletion_result = team_service.roster.remove_token(token=token)
        if deletion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=deletion_result.exception
                    )
                )
            )
        
        square.occupant = token
        token.positions.push_coord(square.coord)
        
        square.state = SquareState.SINGLE_OCCUPANT
        token.board_state = TokenBoardState.FORMED_ON_BOARD
        
    
    @LoggingLevelRouter.monitor
    def process_square_occupation(self, square: Square, token: Token, token_service: TokenService):
        method = "squareService.processSquareOccupation"
        
        
    @LoggingLevelRouter.monitor
    def process_square_evacution(self, square: Square):
        method = "squareService.processSquareEvacuation"
        
        # Handle the case that the square is not certified as safe.
        validation = self.validator.validate(candidate=square)
        if validation.is_failure:
            return SquareServiceExce