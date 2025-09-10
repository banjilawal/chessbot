from enum import Enum

from chess.common.result import Result
from assurance.throw_helper import ThrowHelper
from assurance.validators.side import SideValidator
from chess.competitor.model import Competitor
from chess.config.game import SideProfile
from chess.creator.builder.competitor import CompetitorBuilder
from chess.creator.emit import id_emitter
from chess.side.team import Side


class SideBuilder(Enum):

    @staticmethod
    def build(side_id:int=id_emitter.side_id, controller:Competitor=CompetitorBuilder.build().payload, profile:SideProfile=SideProfile.WHITE) -> Result[Side]:
        try:
            candidate = Side(side_id=side_id, controller=controller, profile=profile)
            validation = SideValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(SideBuilder, validation)
            return validation
        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = SideBuilder.build()
    if build_result.is_success():
        side = build_result.payload
        print(f"Successfully built side: {side}")
    else:
        print(f"Failed to build side: {build_result.exception}")

    build_result = SideBuilder.build(-1)
    if build_result.is_success():
        side = build_result.payload
        print(f"Successfully built side: {side}")
    else:
        print(f"Failed to build side: {build_result.exception}")

if __name__ == "__main__":
    main()