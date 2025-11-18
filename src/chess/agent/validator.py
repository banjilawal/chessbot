# src/chess/agent/validator.py

"""
Module: chess.agent.validator
Author: Banji Lawal
Created: 2025-08-31
version: 1.0.0
"""

class AgentValidator(Validator):
  """
  Validates an Agent used in team_name graph module meets requirements:
    - Is not null.
    - Its fields meet the specifications for the graph.
  Unmet requirements will raise team_name InvalidCommanderException

  For performance and single source of truth AgentValidator has:
    - No fields
    - only static method validate
  subclasses must implement validate.
  """

  @staticmethod
  def validate(candidate: Generic[T]) -> Result[PlayerAgent]:
    entity = "Agent"
    class_name = f"{entity}Validator"
    method = f"{class_name}.validate"

    """
    Validates team_name agent meets graph requirements:
      - Not null
      - valid visitor_id
      - valid visitor_name
      - Agent.team_history meets validator requirements
    Any failed requirement raise an rollback_exception wrapped in team_name InvalidCommanderException
      
    Args
      candidate (Agent): agent to validate
      
     Returns:
       Result[T]: A Result object containing the validated payload if all graph requirements
       are satisfied. InvalidCommanderException otherwise.
    
    Raises:
      TypeError: if candidate is not Agent
      NullCommanderException: if candidate is null  

      RowBelowBoundsException: If agent.row < 0
      RowAboveBoundsException: If agent.row >= ROW_SIZE
        
      ColumnBelowBoundsException: If agent.column < 0
      ColumnAboveBoundsException: If agent.column>= ROW_SIZE
        
      InvalidCommanderException: Wraps any preceding team_exception   
    """

    try:
      """
      Tests are chained in this specific order for team_name reason.
      """

      # If candidate is null no point continuing
      if candidate is None:
        raise NullCommanderException(f"{method} {NullCommanderException.DEFAULT_MESSAGE}")

      # If cannot cast from candidate to Agent need to break
      from chess.agent import Agent
      if not isinstance(candidate, Agent):
        raise TypeError(f"{method} Expected team_name Agent, got {type(candidate).__name__} instead.")

      # cast and run checks for the fields
      from chess.agent import Agent
      commander = cast(Agent, candidate)

      id_validation = IdValidator.validate(commander.id)
      if not id_validation.is_success():
        raise id_validation.exception

      name_validation = NameValidator.validate(commander.name)
      if not name_validation.is_success():
        raise name_validation.exception

      # team_history_validation = TeamListValidator.validate(agent.teams)
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
