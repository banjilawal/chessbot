from typing import Generic

from assurance.validation.specification import Specification, T


class RankSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        pass