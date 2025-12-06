# src/chess/game/builder.builder.py

"""
Module: chess.game.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.agent import Agent, AgentService, UniqueAgentDataService
from chess.board import BoardService
from chess.team import Team, UniqueTeamDataService
from chess.game import Game, GameBuildFailedException
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter, id_emitter


class GameBuilder(Builder[Game]):
    """
    # ROLE: Builder, Data Integrity Guarantor
  
    # RESPONSIBILITIES:
    Produce Game instances whose integrity is always guaranteed. If any attributes
    do not pass their integrity checks, send an exception instead.
  
    # PROVIDES:
    BuildResult[Game] containing either:
        - On success: Game in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    None
    
    # CONSTRUCTOR:
    None
    
    # CLASS METHODS:
        ## build signature
              build(
                    id: int.
                    white_player: Agent,
                    black_player: Agent,
                    board: BoardService = BoardService(),
                    players: UniqueAgentDataService = UniqueAgentDataService(),
                ) -> BuildResult[Game]:
        For ease of use and cleaner code dependencies are given default values.
    
    # INSTANCE METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            white_player: Agent,
            black_player: Agent,
            id: int = id_emitter.service_id,
            board: BoardService = BoardService(),
            identity_service: IdentityService = IdentityService(),
            agent_data: UniqueAgentDataService = UniqueAgentDataService(),
    ) -> BuildResult[Game]:
        """
        # ACTION:
        1.  Check ID safety with IdentityService.validate_id.
        2.  Check schema correctness with GameSchemaValidator.validate.
        3.  Check agent safety with PlayAgentService.validate_player.
        4.  If any check fails, return the exception inside a BuildResult.
        5.  When all checks create a new Game object.
        6.  If the game is not in actor's game_assignments use their game_stack to add it.
    
        # PARAMETERS:
            *   id (int)
            *   white_player (Agent)
            *   black_player (GameSchema)
            *   identity_service (IdentityService)
            *   agent_certifier (AgentService)
            *   schema_validator (GameSchemaValidator)
        All Services have default values to ensure they are never null.
        
        # Returns:
        BuildResult[Game] containing either:
            - On success: Game in the payload.
            - On failure: Exception.
    
        RAISES:
            *   GameBuildFailedException
        """
        method = "GameBuilder.builder"
        
        try:
            # Start the error detection process.
            id_validation = identity_service.validate_id(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            white_player_validation = agent_data.service.validator.validate(white_player)
            if white_player_validation.is_failure():
                return BuildResult.failure(white_player_validation.exception)
            
            team = white_player.team_assignments.team_data_service.s
            
            black_player_validation = agent_data.service.validator.validate(black_player)
            if black_player_validation.is_failure():
                return BuildResult.failure(black_player_validation.exception)
            
            if not agent_data.size != 0:
                return BuildResult.failure(
                    GameAlreadyHasPlayersException(f"{method}: {GameAlreadyHasPlayersException.DEFAULT_MESSAGE}")
                )
            
            insertion_result = agent_data.push_unique(white_player_validation.payload)
            if insertion_result.is_failure():
                return BuildResult.failure(insertion_result.exception)
            
            insertion_result = agent_data.push_unique(black_player_validation.payload)
            if insertion_result.is_failure():
                return BuildResult.failure(insertion_result.exception)
            
            # If no errors are detected build the Game object.
            
            # If the game is not in Agent.game_assignments register it.
            if game not in agent.games:
                agent.game_assignments.push_unique(game)
            # Send the successfully built and registered Game object inside a BuildResult.
            return BuildResult.success(game)
        
        # Finally return a BuildResult containing any unhandled exceptions insided an
        # GameBuildFailedException
        except Exception as ex:
            return BuildResult.failure(
                GameBuildFailedException(ex=ex, message=f"{method}: {GameBuildFailedException.DEFAULT_MESSAGE}")
            )
