# from typing import Generic
#
# from assurance.result.base import Result
# # from assurance.validators.base import Validator, T
# # from chess.validation.base import Rank
#
#
from typing import Generic, TypeVar

from chess.common.validator import Validator
from chess.common import Result
from chess.rank import Rank
T = TypeVar('T')

class RankValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Rank]:
        entity = "Rank"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"
        return Result()
