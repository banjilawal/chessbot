

from typing import cast, Generic, TYPE_CHECKING, TypeVar

from chess.system import Result, Validator, IdValidator, InvalidIdException, InconsistentCollectionException
from chess.team import Team, NullTeamException, NullTeamSchemaException, InvalidTeamException
from chess.commander import Commander, CommanderValidator, InvalidCommanderException, \
  InvalidCommanderAssignmentException
from chess.team.search import TeamSearchContext

T = TypeVar('T')

class PieceSearchContextValidator(Validator):


  @staticmethod
  def validate(candidate: TeamSearchContext) -> Result[TeamSearchContext]:

    method = "TeamValidator.validate"

    try:
      if candidate is None:
        raise NullTeamException(f"{method} {NullTeamException.DEFAULT_MESSAGE}")

      from chess.team import Team
      if not isinstance(candidate, Team):
        raise TypeError(f"{method} Expected team_name Team, got {type(candidate).__name__} instead.")

      team = cast(Team, candidate)

      if team.schema is None:
        raise NullTeamSchemaException(f"{method}: {NullTeamSchemaException.DEFAULT_MESSAGE}")

      id_validation = IdValidator.validate(team.id)
      if not id_validation.is_success():
        raise InvalidIdException(f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")

      commander_validation = CommanderValidator.validate(team.commander)
      if not commander_validation.is_success():
        raise InvalidCommanderException(f"{method}: {InvalidCommanderException.DEFAULT_MESSAGE}")

      commander = cast(Commander, commander_validation.payload)
      if team.commander != commander:
        raise InvalidCommanderAssignmentException(
          f"{method}: {InvalidCommanderAssignmentException.DEFAULT_MESSAGE}"
        )

      if team not in commander.teams.items:
        raise InconsistentCollectionException(
          f"{method}: [Team-Not-In-Commander-History] {RelationshipException.DEFAULT_MESSAGE}"
        )

      return Result(payload=team)

    except (
        TypeError,
        NullTeamException,
        InvalidIdException,
        NullTeamSchemaException,
        InvalidCommanderException,
        InconsistentCollectionException,
        InvalidCommanderAssignmentException,
    ) as e:
      raise InvalidTeamException(f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}") from e

    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidTeamException(f"An unexpected error occurred during validate: {e}") from e

#
# def main():
#
#   from chess.commander.commander import Human
#   person = Human(1, "person")
#
#   from chess.team_name import Team
#   team_name = Team(visitor_team_id=1, controller=person, schema=TeamProfile.BLACK)
#
#
# if __name__ == "__main__":
#   main()