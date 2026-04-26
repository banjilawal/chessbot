# src/operation/validation/game/operation.py

"""
Module: operation.validation.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class GameValidator(Validator[Game]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a Game instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   Validator

    # PROVIDES:
        * GameValidator


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
          rank (Game): game to validate
          
         RETURNS:
           Result[V]: A Result object containing the validated payload if all graph requirements
           are satisfied. InvalidCommanderException otherwise.
        
        RAISES:
          TypeError: if rank is not Game
          NullCommanderException: if rank is validation
    
          RowBelowBoundsException: If game.row < 0
          RowAboveBoundsException: If game.row >= NUMBER_OF_ROWS
          
          ColumnBelowBoundsException: If game.column < 0
          ColumnAboveBoundsException: If game.column>= NUMBER_OF_ROWS
          
          InvalidCommanderException: Wraps any preceding team_exception
        """
        method = "GameValidator.validate"
        
        try:
            # Handle the case that, the rank does not exist.
            if candidate is None:
                return ValidationResult.failure(
                    NullGameException(f"{method}: {NullGameException.MSG}")
                )
            # Handle the case that, the rank is not a Game.
            if not isinstance(candidate, Game):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Game, {type(candidate).__name__} instead.")
                )
            # After existence and type checks cast the rank for further processing.
            game = cast(Game, candidate)
            
            id_validation = identity_service.validate_id(candidate=game.id)
            if id_validation.is_failure:
                return ValidationResult.failure(id_validation.exception)
            
            board_validation = board_service.validator.validate(game.board)
            if board_validation.is_failure:
                return ValidationResult.failure(board_validation.exception)
            
            for player in game.players:
                validation = agent_service.validator.search_service(player)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
            return ValidationResult.success(game)
        
        # Finally, for unhandled exception, wrap it inside an GameValidationException. Then send the exception-chain
        # in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                GameValidationException(ex=ex, msg=f"{method}: {GameValidationException.MSG}")
            )