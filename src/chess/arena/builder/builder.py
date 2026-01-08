# src/chess/arena/builder.py

"""
Module: chess.arena.builder
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from typing import List

from chess.team import Team
from chess.board import Board
from chess.agent import PlayerAgent, AgentService
from chess.arena import Arena, ArenaBuildFailedException, DuplicatePlayerInArenaException
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter, ValidationResult, id_emitter


class ArenaBuilder(Builder[Arena]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce Arena instances whose integrity is guaranteed at creation.
    2.  Manage construction of Arena instances that can be used safely by the client.
    3.  Ensure params for Arena creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.
    
    # PARENT:
        *   Builder

    # PROVIDES:
        *   ArenaBuilder

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
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
        2.  Use arena_variety to pick which builder method will create the concrete Arena object.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   arena_variety (ArenaVariety)
            *   engine_service (Optional[EngineService])

        # RETURNS:
        ValidationResult[Arena] containing either:
            - On success: Arena in the payload.
            - On failure: Exception.

        # RAISES:
            *   ArenaBuildFailedException
        """
        method = "ArenaBuilder.build"
        try:
            # Ensure the id is safe to use.
            id_validation = identity_service.validate_id(candidate=id)
            if id_validation.is_failure:
                return BuildResult.failure(id_validation.exception)
            
            # Verify the board.
            board_validation = board_service.validator.validate(candidate=board)
            if board_validation.is_failure:
                return BuildResult.failure(board_validation.exception)
            
            return BuildResult.success(payload=Arena(id=id, board=board))
        
        # The flow should only get here if the logic did not route all the types of concrete Arenas.
        # In that case wrap the unhandled exception inside an ArenaBuildFailedException then, return
        # the exception chain inside a ValidationResult.
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                ArenaBuildFailedException(ex=ex, message=f"{method}: {ArenaBuildFailedException.DEFAULT_MESSAGE}")
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
            # Perform the basic player safety validation.
            for player in players:
                validation = player_service.validator.validate(candidate=player)
                if validation.failure:
                    return ValidationResult.failure(validation.exception)
            # Handle the case the agents are the same.
            if players[0] == players[1]:
                return ValidationResult.failure(
                    DuplicatePlayerInArenaException(f"{method}: {DuplicatePlayerInArenaException.DEFAULT_MESSAGE}")
                )
            # After individual piece integrity certifcation and uniqueness verification send a success result.
            return ValidationResult.success(payload=players)
        
        # Finally, catch any missed exception, wrap an ArenaBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                ArenaBuildFailedException(ex=ex, message=f"{method}: {ArenaBuildFailedException.DEFAULT_MESSAGE}")
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
            build_result = agent.team_assignments.team_service.builder.build(
                arena=arena,
                player=agent,
                team_schema=team_schema
            )
            if build_result.failure:
                return BuildResult.failure(build_result.exception)
            
            
            
            
        return BuildResult.success(payload=teams)
    