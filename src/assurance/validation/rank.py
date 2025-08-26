from typing import Generic

from assurance.result.base import Result
from assurance.validation.base import Specification, T
from chess.rank.base import Rank


class RankSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[Rank]:
        pass