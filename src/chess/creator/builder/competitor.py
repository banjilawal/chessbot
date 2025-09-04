from enum import Enum

from assurance.result.base import Result
from assurance.throw_helper import ThrowHelper
from assurance.validators.competitor import CompetitorValidator
from chess.creator.emit import id_emitter
from chess.competitor.model import Competitor, HumanCompetitor
from chess.randomize.competitor import RandomName


class CompetitorBuilder(Enum):

    @staticmethod
    def build(competitor_id:int=id_emitter.person_id, name:str="person") -> Result[Competitor]:
        try:
            candidate = HumanCompetitor(competitor_id=competitor_id, name=name)
            validation = CompetitorValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(CompetitorBuilder, validation)
            return validation
        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = CompetitorBuilder.build(competitor_id=id_emitter.person_id, name=RandomName.person())
    if build_result.is_success():
        competitor = build_result.payload
        print(f"Successfully built competitor: {competitor}")
    else:
        print(f"Failed to build competitor: {build_result.exception}")

    build_result = CompetitorBuilder.build(-1,  4)
    if build_result.is_success():
        competitor = build_result.payload
        print(f"Successfully built competitor: {competitor}")
    else:
        print(f"Failed to build competitor: {build_result.exception}")

if __name__ == "__main__":
    main()