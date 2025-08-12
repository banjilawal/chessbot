from typing import Generic

from assurance.validation.validator import Validator, T


class CoordinateValidator(Validator):

    @staticmethod
    def is_valid(item: Generic[T]) -> bool:
        pass