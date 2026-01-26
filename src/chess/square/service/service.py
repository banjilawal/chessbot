# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.square.service.exception.insertion import OccupiedSquareCannotRecieveFormationException
from chess.square.service.exception.occupant.add.full import CannotEnterOccupiedSquareException
from chess.square.state import SquareState
from chess.system import (
    DeletionResult, EntityService, InsertionResult, LoggingLevelRouter, NUMBER_OF_ROWS,
    UpdateResult, id_emitter
)
from chess.square import (
    AddingFormationToSquareFailedException, AddingSquareOccupantFailedException, DisabledTokenOccupyingSquareException,
    NothingToRemoveFromEmptySquareException, RemovingSquareOccupantFailedException, Square, SquareBuilder,
    SquareServiceException,
    SquareTokenRelationAnalyzer, SquareValidator, TokenEnteringSquareOnWrongBoardException,
    TokenEnteringWrongOpeningSquareException
)
from chess.team import FriendCannotCaptureFriendException, Team, TeamService
from chess.token import (
    CombatantActivityState, CombatantToken, KingToken, Token, TokenBoardState, TokenContext,
    TokenDoesNotExistForRemovalException,
    TokenService
)


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
    _square_token_relation_analyzer: SquareTokenRelationAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: SquareBuilder = SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
            relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer(),
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
        self._square_token_relation_analyzer = relation_analyzer
    
    @property
    def builder(self) -> SquareBuilder:
        """get SquareBuilder"""
        return cast(SquareBuilder, self.entity_builder)
    
    @property
    def validator(self) -> SquareValidator:
        """get SquareValidator"""
        return cast(SquareValidator, self.entity_validator)
    
    @property
    def square_token_relation_analyzer(self) -> SquareTokenRelationAnalyzer:
        return self._square_token_relation_analyzer
    
    @LoggingLevelRouter.monitor
    def empty_square_by_token_search(self, token: Token) -> DeletionResult[Token]:
        method = "SquareService.empty_square_by_token_search"
        
        # Handle the case that the square is not certified safe.
        validation = self.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=RemovingSquareOccupantFailedException(
                        message=f"{method}: {RemovingSquareOccupantFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the square is empty.
        if square.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=RemovingSquareOccupantFailedException(
                        message=f"{method}: {RemovingSquareOccupantFailedException.ERROR_CODE}",
                        ex=NothingToRemoveFromEmptySquareException(
                            f"{method}: {NothingToRemoveFromEmptySquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
    
    @LoggingLevelRouter.monitor
    def remove_occupant_from_square(self, square: Square) -> DeletionResult[Token]:
        method = "SquareService.remove_occupant_from_square"
        
        # Handle the case that the square is not certified safe.
        validation = self.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=RemovingSquareOccupantFailedException(
                        message=f"{method}: {RemovingSquareOccupantFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the square is empty.
        if square.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=RemovingSquareOccupantFailedException(
                        message=f"{method}: {RemovingSquareOccupantFailedException.ERROR_CODE}",
                        ex=NothingToRemoveFromEmptySquareException(
                            f"{method}: {NothingToRemoveFromEmptySquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Process removal if the square is occupied.
        token = square.occupant
        square.occupant = None
        square.state = SquareState.EMPTY
        DeletionResult.success(payload=token)
    
    @LoggingLevelRouter.monitor
    def add_occupant_to_square(
            self,
            square: Square,
            token: Token,
            token_service: TokenService = TokenService()
    ) -> InsertionResult[Square]:
        method = "SquareService.add_occupant_to_square"
        
        # Handle the case that the square is not certified safe.
        square_validation = self.validator.validate(candidate=square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # Handle the case that the square is occupied.
        if square.is_occupied:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=CannotEnterOccupiedSquareException(
                            f"{method}: {CannotEnterOccupiedSquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the token is not certified safe.
        token_validation = token_service.validator.validate(candidate=token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=token_validation.exception
                    )
                )
            )
        # Handle the case that the token belongs to a different board
        if token.team.board != square.board:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=TokenEnteringSquareOnWrongBoardException(
                            f"{method}: {TokenEnteringSquareOnWrongBoardException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the token is disabled
        if token.is_disabled:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=DisabledTokenOccupyingSquareException(
                            f"{method}: {DisabledTokenOccupyingSquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the token has not been placed on the board.
        if token.has_not_been_formed:
            return self._add_unformed_token(square=square, token=token)
        
        square.occupant = token
        square.state = SquareState.OCCUPIED
        token.positions.push_coord(square.coord)
        return InsertionResult.success(payload=token)
    
    @LoggingLevelRouter.monitor
    def _add_unformed_token(self, square: Square, token: Token,) -> InsertionResult[Square]:
        method = "SquareService.add_unformed_token"
        
        # Handle the case that the token belongs to a different square.
        if square != token.opening_square:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=TokenEnteringWrongOpeningSquareException(
                            f"{method}: {TokenEnteringWrongOpeningSquareException.}"
                        )
                    )
                )
            )
        # Form the token.
        square.occupant = token
        square.state = SquareState.OCCUPIED
        token.positions.push_coord(square.coord)
        token.board_state = TokenBoardState.FORMED_ON_BOARD
        
        if isinstance(token, KingToken)

        
        
    
    @LoggingLevelRouter.monitor
    def accept_from_roster(
            self,
            team: Team,
            square: Square,
            team_service: TeamService = TeamService()
    ) -> InsertionResult[Square]:
        method = "SquareService.accept_from_roster"
        
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
        # Handle the case that the team has been assigned to a different board.
        if square.board != team.board:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=TeamAndSquareNotOnSameBoardException(
                            f"{method}: {TeamAndSquareNotOnSameBoardException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the square is not empty
        if square.is_occupied:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=OccupiedSquareCannotRecieveFormationException(
                            f"{method}: {OccupiedSquareCannotRecieveFormationException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        search_result = team_service.roster.search_for_token(context=TokenContext(opening_square=square))
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
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
        # Handle the case that no token opens with the square
        if search_result.is_empty:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=TokenDoesNotExistForRemovalException(
                            f"{method}: {TokenDoesNotExistForRemovalException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        token = cast(Token, search_result.payload[0])
        
        # Handle the case that the token has been already placed on the board.
        if token.board_state != TokenBoardState.NEVER_BEEN_PLACED:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingFormationToSquareFailedException(
                        message=f"{method}: {AddingFormationToSquareFailedException.ERROR_CODE}",
                        ex=CannotFormTokenAlreadyOnSquareException(
                            f"{method}: {CannotFormTokenAlreadyOnSquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        deletion_result = team_service.roster.remove_token(token=token)
        
        # Handle the case that the deletion is not completed.
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
        square.occupant = deletion_result.payload
        token.positions.push_coord(square.coord)
        
        square.state = SquareState.OCCUPIED
        token.board_state = TokenBoardState.FORMED_ON_BOARD
        return InsertionResult.success(payload=square)
        
    @LoggingLevelRouter.monitor
    def process_square_occupation(self, square: Square, token: Token, token_service: TokenService):
        method = "squareService.processSquareOccupation"
        
        
    @LoggingLevelRouter.monitor
    def process_square_evacuation(self, square: Square):
        method = "squareService.processSquareEvacuation"
        
        # Handle the case that the square is not certified as safe.
        validation = self.validator.validate(candidate=square)
        if validation.is_failure:
            return SquareServiceExce