from typing import Generic

from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.rank.base import Rank


class RankValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Rank]:
        entity = "Rank"
        class_name = f"{entity}Specification"
        method = f"{class_name}.is_satisfied_by"
        pass