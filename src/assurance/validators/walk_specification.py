from typing import Generic

from assurance.result.base import Result
from assurance.validators.base import Validator, T


class WalkValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Walk]:
        pass