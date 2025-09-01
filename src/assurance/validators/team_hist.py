from typing import Generic, cast

from assurance.exception.validation.team import TeamHistoryValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from assurance.validators.team import TeamValidator
from chess.exception.null.team_stack import NullTeamHistory

from chess.exception.stack import CorruptedStackException, StackSizeConflictException
from chess.exception.team_hist import CurrentTeamException
from chess.owner.team import TeamHistory


class TeamHistoryValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[TeamHistory]:
        entity = "TeamStack"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a TeamStack meets requirements:
            - Not null
            - TeamStack.items is not null
            - TeamStack.current_team is null if the stack is empty, otherwise is a validated Team
            - if TeamStack.is_empty() is True then current_team.size == 0
            - if TeamStack.is_empty() is False then current_team is not null
            - If TeamStack.is_empty() then current_team is null
          Any failed requirement raise an exception wrapped in a TeamStackValidationException      
            
        Validation tests do not change state so pushes and pops are:
            - Tested in unit tests
            - Owner life-cycles and flows.

        Args
            t (TeamStack): team_stack to validate

         Returns:
             Result[T]: Result instance containing a validated team_stack as payload if validations are satisfied,
             TeamStackValidationException otherwise.

        Raises:
            TypeError: if t is not TeamStack
            NullTeamStackException: if t is null

            InternalStackDataStructureException: If TeamStack.items is null
            InconsistentCurrentTeamException: If current_team does not meet TeamValidator

            TeamStackValidationException: Wraps any preceding exceptions
        """
        try:
            if t is None:
                raise NullTeamHistory(f"{method} {NullTeamHistory.DEFAULT_MESSAGE}")

            if not isinstance(t, TeamHistory):
                raise TypeError(f"{method} Expected a TeamStack, got {type(t).__name__}")

            teams = cast(TeamHistory, t)

            if teams.size() > 0 and teams.is_empty():
                raise StackSizeConflictException(f"{method}: {StackSizeConflictException.DEFAULT_MESSAGE}")

            if teams.is_empty() and teams.current_team is not None:
                raise CurrentTeamException(
                    f"{method}: {CurrentTeamException.DEFAULT_MESSAGE}"
                )

            if teams.current_team is None and not teams.is_empty():
                raise CurrentTeamException(
                    f"{method} {CurrentTeamException.DEFAULT_MESSAGE}"
                )

            if teams.items is None:
                raise CorruptedStackException(f"{method} {CorruptedStackException.DEFAULT_MESSAGE}")

            current_team = teams.current_team

            if (
                current_team is not None and
                not TeamValidator.validate(current_team).is_success()
            ):
                raise CurrentTeamException(f"{method} {CurrentTeamException.DEFAULT_MESSAGE}")

            return Result(payload=teams)

        except (
            TypeError,
            NullTeamHistory,
            StackSizeConflictException,
            CurrentTeamException
        ) as e:
            raise TeamHistoryValidationException(
                f"{method}: {TeamHistoryValidationException.DEFAULT_MESSAGE}"
            ) from e
#