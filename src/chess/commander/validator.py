from typing import cast, Generic, TYPE_CHECKING

from chess.commander.exception import CommanderHistoryException
from chess.system import Result, Validator, IdValidator, NameValidator
from chess.exception import NameValidationException, IdValidationException
from chess.commander import Commander, NullCommanderException, InvalidCommanderException


class CommanderValidator(Validator):
  """
  Validates an Commander used in team graph module meets requirements:
    - Is not null.
    - Its fields meet the specifications for the graph.
  Unmet requirements will raise team InvalidCommanderException

  For performance and single source of truth CommanderValidator has:
    - No fields
    - only static method validate
  subclasses must implement validate.
  """

  @staticmethod
  def validate(candidate: Generic[T]) -> Result[Commander]:
    entity = "Commander"
    class_name = f"{entity}Validator"
    method = f"{class_name}.validate"

    """
    Validates team commander meets graph requirements:
      - Not null
      - valid id
      - valid name
      - Commander.team_history meets validator requirements
    Any failed requirement raise an rollback_exception wrapped in team InvalidCommanderException
      
    Args
      candidate (Commander): commander to validate
      
     Returns:
       Result[T]: A Result object containing the validated payload if all graph requirements
       are satisfied. InvalidCommanderException otherwise.
    
    Raises:
      TypeError: if candidate is not Commander
      NullCommanderException: if candidate is null  

      RowBelowBoundsException: If commander.row < 0
      RowAboveBoundsException: If commander.row >= ROW_SIZE
        
      ColumnBelowBoundsException: If commander.column < 0
      ColumnAboveBoundsException: If commander.column>= ROW_SIZE
        
      InvalidCommanderException: Wraps any preceding team_exception   
    """

    try:
      """
      Tests are chained in this specific order for team reason.
      """

      # If candidate is null no point continuing
      if candidate is None:
        raise NullCommanderException(f"{method} {NullCommanderException.DEFAULT_MESSAGE}")

      # If cannot cast from candidate to Commander need to break
      from chess.commander import Commander
      if not isinstance(candidate, Commander):
        raise TypeError(f"{method} Expected team Commander, got {type(candidate).__name__}")

      # cast and run checks for the fields
      from chess.commander import Commander
      commander = cast(Commander, candidate)

      id_validation = IdValidator.validate(commander.id)
      if not id_validation.is_success():
        raise id_validation.exception

      name_validation = NameValidator.validate(commander.name)
      if not name_validation.is_success():
        raise name_validation.exception

      # team_history_validation = TeamListValidator.validate(commander.teams)
      # if not team_history_validation.is_success():
      #   raise team_history_validation.err

      # Return the notification if checks passed
      return Result(payload=commander)

    except (
        TypeError,
        NullCommanderException,
        IdValidationException,
        NameValidationException,
        CommanderHistoryException
    ) as e:
      raise InvalidCommanderException(f"{method}: {InvalidCommanderException.DEFAULT_MESSAGE}") from e


    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidCommanderException(f"{method}: {e}") from e
