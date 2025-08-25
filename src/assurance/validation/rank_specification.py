from typing import Generic

from assurance.result.base_result import Result
from assurance.validation.specification import Specification, T
from chess.rank.rank import Rank


class RankSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[Rank]:
        pass