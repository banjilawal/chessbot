from typing import cast, Generic, TYPE_CHECKING

from chess.commander.exception import TeamListException
from chess.system import Result, Validator, IdValidator, NameValidator
from chess.exception import NameValidationException, IdValidationException
from chess.commander import Commander, NullCommanderException, InvalidCommanderException


class CommanderValidator(Validator):
    """
    Validates an Commander used in a domain module meets requirements:
        - Is not null.
        - Its fields meet the specifications for the domain.
    Unmet requirements will raise a InvalidCommanderException

    For performance and single source of truth CommanderValidator has:
        - No fields
        - only static method validate
    subclasses must implement validate.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result[Commander]:
        entity = "Commander"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a commander meets domain requirements:
            - Not null
            - valid id
            - valid name
            - Commander.team_history meets validator requirements
        Any failed requirement raise an team_exception wrapped in a InvalidCommanderException
            
        Args
            t (Commander): commander to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if all domain requirements 
             are satisfied. InvalidCommanderException otherwise.
        
        Raises:
            TypeError: if t is not Commander
            NullCommanderException: if t is null   

            RowBelowBoundsException: If commander.row < 0
            RowAboveBoundsException: If commander.row >= ROW_SIZE
                
            ColumnBelowBoundsException: If commander.column < 0
            ColumnAboveBoundsException: If commander.column>= ROW_SIZE
                
            InvalidCommanderException: Wraps any preceding team_exception     
        """

        try:
            """
            Tests are chained in this specific order for a reason.
            """

            # If t is null no point continuing
            if t is None:
                raise NullCommanderException(f"{method} {NullCommanderException.DEFAULT_MESSAGE}")

            # If cannot cast from t to Commander need to break
            from chess.commander import Commander
            if not isinstance(t, Commander):
                raise TypeError(f"{method} Expected a Commander, got {type(t).__name__}")

            # cast and run checks for the fields
            from chess.commander import Commander
            commander = cast(Commander, t)

            id_validation = IdValidator.validate(commander.id)
            if not id_validation.is_success():
                raise id_validation.exception

            name_validation = NameValidator.validate(commander.name)
            if not name_validation.is_success():
                raise name_validation.exception

            # team_history_validation = TeamListValidator.validate(commander.teams)
            # if not team_history_validation.is_success():
            #     raise team_history_validation.exception

            # Return the result if checks passed
            return Result(payload=commander)

        except (
                TypeError,
                NullCommanderException,
                IdValidationException,
                NameValidationException,
                TeamListException
        ) as e:
            raise InvalidCommanderException(f"{method}: {InvalidCommanderException.DEFAULT_MESSAGE}") from e


        # This block catches any unexpected exceptions
        # You might want to log the exception here before re-raising
        except Exception as e:
            raise InvalidCommanderException(f"An unexpected error occurred during validation: {e}") from e
