# src/chess/team/order/number_bounds_validator.py

"""
Module: chess.team.order.number_bounds_validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast, Any

from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.team import InvalidBattleOrderException, NullBattleOrderException, BattleOrder


class BattleOrderValidator(Validator[BattleOrder]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a BattleOrder instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[BattleOrder]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check the candidate is a BattleOrder enum
        3.  If both checks pass cast the candidate to a BattleOrder and return in a
            ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[BattleOrder] containing either:
            - On success:   BattleOrder in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullBattleOrderException
            *   InvalidBattleOrderException
        """
        method = "BattleOrderValidator.validate"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullBattleOrderException(f"{method} {NullBattleOrderException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, BattleOrder):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected BattleOrder, got {type(candidate).__name__} instead.")
                )
            # If no errors are detected cast the candidate to a BattleOrder object then return in
            # a ValidationResult.
            return ValidationResult.success(cast(BattleOrder, candidate))
        
        # Finally, if there is an unhandled exception Wrap an InvalidPieceException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBattleOrderException(ex=ex, message=f"{method} {InvalidBattleOrderException.DEFAULT_MESSAGE}")
            )
