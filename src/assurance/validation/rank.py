from typing import Generic

from assurance.result.base import Result
from assurance.validation.base import Specification, T
from chess.rank.base import Rank


class RankSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[Rank]:
        entity = "Rank"
        class_name = f"{entity}Specification"
        method = f"{class_name}.is_satisfied_by"
        pass