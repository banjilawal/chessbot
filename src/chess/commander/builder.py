# chess/commander/builder.py

"""
Module: `chess.commander.builder`
Author: Banji Lawal
Created: 2025-10-03
Updated: 2025-10-04
version: 1.0.0

 Provides: Create concrete subclasses of `Commander`

Contains:
  * `CommanderBuilder`
"""

from typing import Optional

from chess.system import LoggingLevelRouter, NameValidator, InvalidNameException, BuildResult, Builder
from chess.commander import Commander, Human, Bot, CommanderBuildFailedException
from chess.engine import DecisionEngine


class CommanderBuilder(Builder[Commander]):
  """
  Responsible for safely constructing `Commander` instances.
  """

  @classmethod
  def build(cls, name: str, engine: Optional[DecisionEngine]=None) -> BuildResult[Commander]:
    """
    Constructs team new `Commander` that works correctly.

    Args:
      `name` (`str`): Must pass `NameValidator` checks.
      `engine` (DecisionEngine): The engine used to determine how to play.`

    Returns:
    BuildResult[Commander]: A `BuildResult` containing either:
      - On success: A valid `Commander` instance in the payload
      - On failure: Error information and error details

    Raises:
    `CommanderBuildFailedException`: Wraps any exceptions raised build. These are:
      * `InvalidIdException`: if `commander_id` fails validate checks.
      * `InvalidNameException`: if `name` fails validate checks.
      * `EngineValidationException`: If `engine` is not null and fails validate checks.
    """
    method = "CommanderBuilder.build"

    try:
      # id_validation = IdValidator.validate(commander_id)
      # if not id_validation.is_success():
      #   LoggingLevelRouter.throw_if_invalid(CommanderBuilder, id_validation.err)
      name_validation = NameValidator.validate(name)
      if not name_validation.is_success():
        LoggingLevelRouter.log_and_raise_error(CommanderBuilder, name_validation.exception)

      if engine is not None and not isinstance(engine, DecisionEngine):
        error = TypeError(f"Expected team Decision, but got {type(engine).__name__}.")
        LoggingLevelRouter.log_and_raise_error(CommanderBuilder, error)

      if engine is not None and isinstance(engine, DecisionEngine):
        return BuildResult(payload=Bot(name=name, engine=engine))

      # If no engine is provided and all the checks are passed, team Human commander is returned
      return BuildResult(payload=Human(name=name))

    except (
      TypeError,
      InvalidNameException
    ) as e:
      raise CommanderBuildFailedException(f"{method}: {e}") from e

    # Catch any unexpected errors with details about type and message
    except Exception as e:
      raise CommanderBuildFailedException(
        f"{method}: Unexpected error ({type(e).__name__}): {e}"
      ) from e
#
#
# def main():
#   build_result = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
#   if build_result.is_success():
#     competitor = build_result.payload
#     print(f"Successfully built competitor: {competitor}")
#   else:
#     print(f"Failed to build competitor: {build_result.err}")
#
#   build_result = CommanderBuilder.build(-1, 4)
#   if build_result.is_success():
#     competitor = build_result.payload
#     print(f"Successfully built competitor: {competitor}")
#   else:
#     print(f"Failed to build competitor: {build_result.err}")
#
# if __name__ == "__main__":
#   main()