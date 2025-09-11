from enum import Enum

from chess.result import Result
from assurance.throw_helper import ThrowHelper
from chess.team.team_validator import TeamValidator
from chess.competitor.commander import Commander
from chess.team.team_profile import TeamProfile
from chess.builder.commander_builder import CommanderBuilder
from chess.common.emit import id_emitter
from chess.side.team import Side


class TeamBuilder(Enum):

    @staticmethod
    def build(side_id:int=id_emitter.side_id, controller:Commander=CommanderBuilder.build().payload, profile:TeamProfile=TeamProfile.WHITE) -> Result[Side]:
        try:
            candidate = Side(side_id=side_id, controller=controller, profile=profile)
            validation = TeamValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(TeamBuilder, validation)
            return validation
        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = TeamBuilder.build()
    if build_result.is_success():
        side = build_result.payload
        print(f"Successfully built side: {side}")
    else:
        print(f"Failed to build side: {build_result.exception}")

    build_result = TeamBuilder.build(-1)
    if build_result.is_success():
        side = build_result.payload
        print(f"Successfully built side: {side}")
    else:
        print(f"Failed to build side: {build_result.exception}")

if __name__ == "__main__":
    main()