# src/chess/game/builder.builder.py

"""
Module: chess.game.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.agent import PlayerAgent, AgentService, UniqueAgentDataService
from chess.board import BoardService
from chess.team import Team, UniqueTeamDataService
from chess.game import Game, GameBuildFailedException
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter, id_emitter


class GameBuilder(Builder[Game]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor
  
    # RESPONSIBILITIES:
    Produce Game instances whose integrity is guaranteed at creation.
    
    # PROVIDES:
    BuildResult[Game] containing either:
        - On success: Game in the payload.
        - On failure: Exception.
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            white_player: PlayerAgent,
            black_player: PlayerAgent,
            id: int = id_emitter.service_id,
            board: BoardService = BoardService(),
            identity_service: IdentityService = IdentityService(),
            agent_service: AgentService = AgentService(),
    ) -> BuildResult[Game]:
        """
        # ACTION:
        1.  Use identity_service to confirm the id is safe.
        2.  Use player_service to validate the white and black players. are safe.
        3.  Certify the BoardService with the BoardServiceCertifier
        4.  If any check fails, return the exception inside a BuildResult.
        5.  When all checks pass create the new Game object.
        6.  Register the game with the white and black owner by pushing onto their respective game stacks.
        7.  Return the Game inside a BuildResult.
    
        # PARAMETERS:
            *   id (int)
            *   white_player (Player)
            *   black_player (GameSchema)
            *   identity_service (IdentityService)
            *   player_service (AgentService)
            *   board_certifier (BoardCertifier)
        All Services have default values to ensure they are never null.
        
        # RETURNS:
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
            
            white_player_validation = agent_service.validator.validate(white_player)
            if white_player_validation.is_failure():
                return BuildResult.failure(white_player_validation.exception)
                
            black_player_validation = agent_service.validator.validate(black_player)
            if black_player_validation.is_failure():
                return BuildResult.failure(black_player_validation.exception)
            
            game = Game(
                id=id,
                white_player=white_player,
                black_player=black_player,
                board=board
            )
            
            
            
            insertion_result = agent_data.push_unique_item(white_player_validation.payload)
            if insertion_result.is_failure():
                return BuildResult.failure(insertion_result.exception)
            
            insertion_result = agent_data.push_unique_item(black_player_validation.payload)
            if insertion_result.is_failure():
                return BuildResult.failure(insertion_result.exception)
            
            # If no errors are detected build the Game object.
            
            # If the game is not in Player.game_assignments register it.
            if game not in player.games:
                player.game_assignments.push_unique_item(game)
            # Send the successfully built and registered Game object inside a BuildResult.
            return BuildResult.success(game)
        
        # Finally return a BuildResult containing any unhandled exception insided an
        # GameBuildFailedException
        except Exception as ex:
            return BuildResult.failure(
                GameBuildFailedException(ex=ex, message=f"{method}: {GameBuildFailedException.DEFAULT_MESSAGE}")
            )
