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
        method = "PlayerService.add_team"
        relation = self.player_team_relation_analyzer.test(
            candidate_primary=player,
            candidate_secondary=team,
            owner_validator=self.validator,
            team_service=team_service,
        )
        if relation.is_failure:
            return InsertionResult.failure(
                PlayerServiceException(
                    message=f"ServiceId:{self.id}, {method}: {PlayerServiceException.ERROR_CODE}",
                    ex=relation.exception
                )
            )
        if relation.does_not_exist:
            return InsertionResult.failure(
                PlayerServiceException(
                    message=f"ServiceId:{self.id}, {method}: {PlayerServiceException.ERROR_CODE}",
                    ex=TeamBelongsToDifferentOwnerException(
                        f"{method}: {TeamBelongsToDifferentOwnerException.DEFAULT_MESSAGE}"
                    )
                )
            )
        if relation.is_success:
            return InsertionResult.failure(
                PlayerServiceException(
                    message=f"ServiceId:{self.id}, {method}: {PlayerServiceException.ERROR_CODE}",
                    ex=AddingDuplicateTeamException(f"{method}: {AddingDuplicateTeamException.DEFAULT_MESSAGE}")
                )
            )
        return player.teams.add_team(team=team)

    
    