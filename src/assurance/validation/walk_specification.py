from typing import Generic

from assurance.validation.specification import Specification, T


class WalkSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        pass