from typing import cast, Generic

from assurance.exception.validation.team_stack import TeamStackValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.exception.null.team_stack import NullTeamStackException
from chess.team.stack import TeamStack


class TeamStackValidator(Validator):
    """
    Validates a TeamStack used in a domain module meets requirements:
        - Is not null.
        - Only Team instances can be added to the stack.
        - Teams cannot be popped from the stack
        - An empty team stack returns null
        - A nonempty stack returns a validated Team
    Unmet requirements will raise a TeamStackValidationException

    For performance and single source of truth TeamStackValidator has:
        - No fields
        - only static method validate
    subclasses must implement validate.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result[TeamStack]:
        entity = "TeamStack"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a teamStack meets domain requirements:
            - Not null
            - row is not null
            - column is not null
            - row is within the bounds of the chess chessboard
            - column is within the bounds of the chess chessboard
        Any failed requirement raise an exception wrapped in a TeamStackValidationException
            
        Args
            t (TeamStack): teamStack to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if all domain requirements 
             are satisfied. TeamStackValidationException otherwise.
        
        Raises:
            TypeError: if t is not TeamStack
            NullTeamStackException: if t is null   

            RowBelowBoundsException: If teamStack.row < 0
            RowAboveBoundsException: If teamStack.row >= ROW_SIZE
                
            ColumnBelowBoundsException: If teamStack.column < 0
            ColumnAboveBoundsException: If teamStack.column>= ROW_SIZE
                
            TeamStackValidationException: Wraps any preceding exception     
        """

        try:
            """
            Tests are chained in this specific order for a reason.
            """

            # If t is null no point continuing
            if t is None:
                raise NullTeamStackException(f"{method} NullTeamStackException.DEFAULT_MESSAGE")

            # If cannot cast from t to TeamStack need to break
            if not isinstance(t, TeamStack):
                raise TypeError(f"{method} Expected a TeamStack, got {type(t).__name__}")

            # cast and run checks for the fields
            team_stack = cast(TeamStack, t)

            if team_stack.is_empty() and team:
                raise NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")

            if teamStack.row < 0:
                raise RowBelowBoundsException(f"{method} {RowBelowBoundsException.DEFAULT_MESSAGE}")

            if teamStack.row >= ROW_SIZE:
                raise RowAboveBoundsException(f"{method} {RowAboveBoundsException.DEFAULT_MESSAGE}")

            if teamStack.column is None:
                raise NullColumnException(f"{method} {NullColumnException.DEFAULT_MESSAGE}")

            if teamStack.column < 0:
                raise ColumnBelowBoundsException(f"{method} {ColumnBelowBoundsException.DEFAULT_MESSAGE}")

            if teamStack.column >= COLUMN_SIZE:
                raise ColumnAboveBoundsException(f"{method} {ColumnAboveBoundsException.DEFAULT_MESSAGE}")

            # Return the result if checks passed
            return Result(payload=teamStack)

        except (
            TypeError,
            NullTeamStackException,

            NullRowException,
            RowBelowBoundsException,
            RowAboveBoundsException,

            NullColumnException,
            ColumnBelowBoundsException,
            ColumnAboveBoundsException
        ) as e:
            raise TeamStackValidationException(
                f"{method}: {TeamStackValidationException.DEFAULT_MESSAGE}"
            ) from e