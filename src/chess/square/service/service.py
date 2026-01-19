# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import cast

from chess.square.service.exception.insertion import OccupiedSquareCannotRecieveFormationException
from chess.square.state import SquareState
from chess.system import EntityService, InsertionResult, LoggingLevelRouter, id_emitter
from chess.square import (
    AddingFormationToSquareFailedException, Square, SquareBuilder, SquareServiceException,
    SquareValidator
)
from chess.team import FriendCannotCaptureFriendException, Team, TeamService
from chess.token import (
    CombatantActivityStatue, CombatantToken, KingToken, Token, TokenBoardState, TokenContext,
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
    
    @LoggingLevelRouter
    def deliver_to_hostages(
            self,
            square: Square,
            enemy_team: Team,
            team_service: TeamService = TeamService()
    ) -> InsertionResult[Token]:
        method = "squareService.deliver_to_hostages"
        
        # Handle the case that the square is not certified safe.
        square_validation = self.validator.validate(candidate=square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=DeliveringHostageFailedException(
                        message=f"{method}: {DeliveringHostageFailedException.ERROR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # Handle the case that the token is not certified safe.
        enemy_team_validation = team_service.validator.validate(candidate=enemy_team)
        if enemy_team_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=DeliveringHostageFailedException(
                        message=f"{method}: {DeliveringHostageFailedException.ERROR_CODE}",
                        ex=enemy_team_validation.exception
                    )
                )
            )
        # Handle the case that the square is not empty
        if square.state == SquareState.EMPTY:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=DeliveringHostageFailedException(
                        message=f"{method}: {DeliveringHostageFailedException.ERROR_CODE}",
                        ex=EmptySquareCannotSendHostageException(
                            f"{method}: {EmptySquareCannotSendHostageException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the token is not an enemy of the team.
        if square.occupant.team == enemy_team:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=DeliveringHostageFailedException(
                        message=f"{method}: {DeliveringHostageFailedException.ERROR_CODE}",
                        ex=CannotPutFriendAmongHostagesException(
                            f"{method}: {CannotPutFriendAmongHostagesExceptionn.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the square's occupant is not a CombatantToken.
        if isinstance(square.occupant, KingToken):
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=DeliveringHostageFailedException(
                        message=f"{method}: {DeliveringHostageFailedException.ERROR_CODE}",
                        ex=KingTokenCannotBeCapturedException(
                            f"{method}: {KingTokenCannotBeCapturedException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        combatant = cast(CombatantToken, square.occupant)
        
        # Handle the case that the combatant has not been captured.
        if combatant.captor is None and combatant.activity_status == CombatantActivityStatue.FREE:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=DeliveringHostageFailedException(
                        message=f"{method}: {DeliveringHostageFailedException.ERROR_CODE}",
                        ex=AddingFreeEnemyToHostagesException(
                            f"{method}: {AddingFreeEnemyToHostagesException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the combatant is already among the hostages.
        if combatant.activity_status == CombatantActivityStatue.REGISTERED_HOSTAGE:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=DeliveringHostageFailedException(
                        message=f"{method}: {DeliveringHostageFailedException.ERROR_CODE}",
                        ex=EnemyAlreadyAmongHostages(
                            f"{method}: {EnemyAlreadyAmongHostages.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        
        square.occupant = None
        insertion_result = enemy_team.hostages.add_prisoner(combatant=combatant)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=DeliveringHostageFailedException(
                        message=f"{method}: {DeliveringHostageFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        hostage = cast(CombatantToken, insertion_result.payload)
        hostage.combatant_status = CombatantActivityStatue.REGISTERED_HOSTAGE
        return InsertionResult.success(payload=hostage)
        

        
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
        return InsertionResult.success(payload=square)
    
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
        if square.state != SquareState.EMPTY:
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
        
        square.state = SquareState.SINGLE_OCCUPANT
        token.board_state = TokenBoardState.FORMED_ON_BOARD
        return InsertionResult.success(payload=square)
        
    
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