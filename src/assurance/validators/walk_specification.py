from typing import Generic

from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.walk.base import Walk


class WalkValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Walk]:
        pass