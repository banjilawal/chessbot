from typing import Generic

from chess.result import Result
from chess.common.validator import Validator, T


class WalkValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Walk]:
        pass