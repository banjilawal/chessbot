# src/chess/player/service/service.py

"""
Module: chess.player.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from typing import cast
from unittest import removeResult

from chess.player import Player, PlayerFactory, PlayerValidator
from chess.player.relation import PlayerTeamRelationAnalyzer
from chess.system import EntityService, InsertionResult, LoggingLevelRouter, Result, id_emitter
from chess.team import Team, TeamService


class PlayerService(EntityService[Player]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Player microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Player state by providing single entry and exit points to Player
        lifecycle.

    # PARENT:
        *   EntityService
    
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See EntityService class for inherited attributes.
    """
    DEFAULT_NAME = "PlayerService"
    _player_team_relation_analyzer: PlayerTeamRelationAnalyzer
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: PlayerFactory = PlayerFactory(),
            validator: PlayerValidator = PlayerValidator(),
            player_team_relation_analyzer: PlayerTeamRelationAnalyzer = PlayerTeamRelationAnalyzer(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (PlayerFactory)
            *   validator (PlayerValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._player_team_relation_analyzer = player_team_relation_analyzer
        
    @property
    def builder(self) -> PlayerFactory:
        """get PlayerBuilder"""
        return cast(PlayerFactory, self.entity_builder)
    
    @property
    def validator(self) -> PlayerValidator:
        """get PlayerValidator"""
        return cast(PlayerValidator, self.entity_validator)
    
    @property
    def player_team_relation_analyzer(self) -> PlayerTeamRelationAnalyzer:
        return self._player_team_relation_analyzer
    
    def add_team(self, player: Player, team: Team, team_service: TeamService = TeamService()) -> InsertionResult[Team]:
        """
        # ACTION:
            1.  If the player_team_relation_result does not return partial registration send an exception chain in
                the InsertionResult.
            2.  Forward the result of player.teams.add_team to the caller.
        # PARAMETERS:
            *   player (Player)
            *   team (Team)
            *   team_service (TeamService)
        # RETURNS:
            *   InsertionResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        # RAISES:
            *   TypeError
            *   PlayerServiceException
            *   TeamInsertionFailedException
            *   AddingDuplicateTeamException
            *   TeamBelongsToDifferentOwnerException
        """
        
        method = "PlayerService.add_team"
        relation = self.player_team_relation_analyzer.analyze(
            candidate_primary=player,
            candidate_secondary=team,
            owner_validator=self.validator,
            team_service=team_service,
        )
        # Handle the case that the relation analysis is not completed.
        if relation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PlayerServiceException(
                    message=f"ServiceId:{self.id}, {method}: {PlayerServiceException.ERROR_CODE}",
                    ex=TeamInsertionFailedException(
                        message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}",
                        ex=relation.exception)
                )
            )
        # Handle the case that the team belongs to a different player.
        if relation.does_not_exist:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PlayerServiceException(
                    message=f"ServiceId:{self.id}, {method}: {PlayerServiceException.ERROR_CODE}",
                    ex=TeamInsertionFailedException(
                        message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}",
                        ex=TeamBelongsToDifferentOwnerException(
                            f"{method}: {TeamBelongsToDifferentOwnerException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the player already has the team.
        if relation.is_success:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PlayerServiceException(
                    message=f"ServiceId:{self.id}, {method}: {PlayerServiceException.ERROR_CODE}",
                    ex=TeamInsertionFailedException(
                        message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}",
                        ex=AddingDuplicateTeamException(f"{method}: {AddingDuplicateTeamException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # Handle the case that pushing the new team on to player's TeamStack fails.
        insertion_result = player.teams.add_team(team=team)
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PlayerServiceException(
                    message=f"ServiceId:{self.id}, {method}: {PlayerServiceException.ERROR_CODE}",
                    ex=TeamInsertionFailedException(
                        message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # If the coord was successfully pushed onto the token's coord stack forward insertion result.
        return insertion_result

    
    