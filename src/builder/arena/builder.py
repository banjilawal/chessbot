# src/builder/arena/builder.py

"""
Module: builder.arena.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from typing import List

from logic.team import Team
from logic.board import Board
from logic.agent import PlayerAgent, AgentService
from logic.arena import Arena, ArenaBuilderException, DuplicatePlayerInArenaException
from system import Builder, BuildResult, IdentityService, LoggingLevelRouter, ValidationResult, id_emitter


class ArenaBuilder(Builder[Arena]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Arena instance is born safe and reliable.

    Attributes:

    Provides:
        -   def build(
                    board: Board,
                    id: int = id_emitter.arena_id,
                    board_service: BoardService = BoardService(),
                    identity_service: IdentityService = IdentityService(),
            ) -> BuildResult[Arena]:

     Super Class:
         Builder
     """
    
    @classmethod
    def build(
            cls,
            board: Board,
            id: int = id_emitter.arena_id,
            board_service: BoardService = BoardService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Arena]:
        """
        # ACTION:
        1.  verify arena_variety is a not-null ArenaVariety object.
        2.  Use arena_variety to pick which build method will create the concrete Arena object.

        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   arena_variety (ArenaVariety)
            *   engine_service (Optional[EngineService])

        # RETURNS:
        ValidationResult[Arena] containing either:
            - On success: Arena in the payload.
            - On failure: Exception.

        Raises:
            *   ArenaBuilderException
        """
        method = "ArenaBuilder.build"
        try:
            # Ensure the id is safe to use.
            id_validation = identity_service.validate_id(candidate=id)
            if id_validation.is_failure:
                return BuildResult.failure(id_validation.exception)
            
            # Verify the board.
            board_validation = board_service.validate.search_service(candidate=board)
            if board_validation.is_failure:
                return BuildResult.failure(board_validation.exception)
            
            return BuildResult.success(payload=Arena(id=id, board=board))
        
        # The flow should only get here if the logic did not route all the types of concrete Arenas.
        # In that case wrap the unhandled exception inside an ArenaBuilderException then, return
        # the exception chain inside a ValidationResult.
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                ArenaBuilderException(ex=ex, msg=f"{method}: {ArenaBuilderException.MSG}")
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _certify_players(
            cls,
            players: List[PlayerAgent],
            player_service: AgentService = AgentService()
    ) -> ValidationResult[List[PlayerAgent]]:
        """"""
        method = "ArenaBuilder._certify_players"
        try:
            # Perform the basic owner safety validation.
            for player in players:
                validation = player_service.validate.search_service(candidate=player)
                if validation.failure:
                    return ValidationResult.failure(validation.exception)
            # Handle the case the agents are the same.
            if players[0] == players[1]:
                return ValidationResult.failure(
                    DuplicatePlayerInArenaException(f"{method}: {DuplicatePlayerInArenaException.MSG}")
                )
            # After individual piece integrity certifcation and uniqueness verification send a success result.
            return ValidationResult.success(payload=players)
        
        # Finally, catch any missed exception, wrap an ArenaBuilderException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                ArenaBuilderException(ex=ex, msg=f"{method}: {ArenaBuilderException.MSG}")
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_arena_teams(
            cls,
            arena: Arena,
            team_param_tuples: List[(PlayerAgent, Schema)],
    ) -> BuildResult[List[Team]]:
        method = "ArenaBuilder._build_teams"
        for param_tuple in team_param_tuples:
            agent, team_schema = param_tuple
            build_result = player.teams.pair_service.factory.search_service(
                arena=arena,
                player=agent,
                team_schema=team_schema
            )
            if build_result.failure:
                return BuildResult.failure(build_result.exception)
            
            
            
            
        return BuildResult.success(payload=teams)
    