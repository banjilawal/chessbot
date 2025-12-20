# src/chess/game/validator/validator.py

"""
Module: chess.game.validator
Author: Banji Lawal
Created: 2025-08-31
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import AgentService
from chess.board import BoardService
from chess.engine.service import EngineService
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.game import (
    Game, GameVariety, GameVarietyNullException, InvalidGameException, MachineGame, NullGameException,
)



class GameValidator(Validator[Game]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Game instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
        * GameValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            board_service: BoardService = BoardService(),
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Game]:
        """
        Validates team_name game meets graph requirements:
          - Not validation
          - valid visitor_id
          - valid visitor_name
          - Game.team_history meets coord_stack_validator requirements
        Any failed requirement raise an exception wrapped in team_name InvalidCommanderException
        
        Args
          candidate (Game): game to validate
          
         Returns:
           Result[V]: A Result object containing the validated payload if all graph requirements
           are satisfied. InvalidCommanderException otherwise.
        
        Raises:
          TypeError: if candidate is not Game
          NullCommanderException: if candidate is validation
    
          RowBelowBoundsException: If game.row < 0
          RowAboveBoundsException: If game.row >= ROW_SIZE
          
          ColumnBelowBoundsException: If game.column < 0
          ColumnAboveBoundsException: If game.column>= ROW_SIZE
          
          InvalidCommanderException: Wraps any preceding team_exception
        """
        method = "GameValidator.validate"
        
        try:
            # Handle the case that the candidate does not exist.
            if candidate is None:
                return ValidationResult.failure(
                    NullGameException(f"{method}: {NullGameException.DEFAULT_MESSAGE}")
                )
            # Handle the case that the candidate is not a Game.
            if not isinstance(candidate, Game):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Game, {type(candidate).__name__} instead.")
                )
            # After existence and type checks cast the candidate for further processing.
            game = cast(Game, candidate)
            
            id_validation = identity_service.validate_id(candidate=game.id)
            if id_validation.is_failure:
                return ValidationResult.failure(id_validation.exception)
            
            board_validation = board_service.validator.validate(game.board)
            if board_validation.is_failure:
                return ValidationResult.failure(board_validation.exception)
            
            for player in game.players:
                validation = agent_service.validator.validate(player)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
            return ValidationResult.success(game)
        
        # Finally, for unhandled exception, wrap it inside an InvalidGameException. Then send the  exception-chain
        # in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidGameException(ex=ex, message=f"{method}: {InvalidGameException.DEFAULT_MESSAGE}")
            )