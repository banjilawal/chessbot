from enum import Enum
from chess.builder import CommanderBuilder
from chess.team import Team, TeamProfile, TeamValidator
from chess.commander import Commander
from chess.common import Result
from assurance import ThrowHelper



class TeamBuilder(Enum):

    @staticmethod
    def build(
        team_id:int=1,
        commander:Commander=CommanderBuilder.build().payload,
        profile:TeamProfile=TeamProfile.WHITE
    ) -> Result[Team]:
        method = "TeamBuilder.build"

        try:
            candidate = Team()
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