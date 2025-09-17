from typing import Generic, cast

from chess.team.team_exception.invalid_team import TeamHistoryValidationException
from chess.result import Result
from chess.common.validator import Validator, T
from chess.exception.null.side_record import NullSideRecordException

from chess.exception.stack_exception import CorruptedStackException, StackSizeConflictException
from chess.commander.team_history_exception import CurrentTeamException
from chess.competitor.side import SideRecord



class SideRecordValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[SideRecord]:
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
          Any failed requirement raise an team_exception wrapped in a TeamStackValidationException      
            
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
                raise NullSideRecordException(f"{method} {NullSideRecordException.DEFAULT_MESSAGE}")

            if not isinstance(t, SideRecord):
                raise TypeError(f"{method} Expected a TeamStack, got {type(t).__name__}")

            teams = cast(SideRecord, t)

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

            # if (
            #     current_team is not None and
            #     not TeamValidator.validate(current_team).is_success()
            # ):
            #     raise CurrentTeamException(f"{method} {CurrentTeamException.DEFAULT_MESSAGE}")

            return Result(payload=teams)

        except (
                TypeError,
                NullSideRecordException,
                StackSizeConflictException,
                CurrentTeamException
        ) as e:
            raise TeamHistoryValidationException(
                f"{method}: {TeamHistoryValidationException.DEFAULT_MESSAGE}"
            ) from e
#