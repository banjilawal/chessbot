from enum import Enum

from chess.scalar import Scalar, ScalarValidator
from chess.common import Result
from assurance import ThrowHelper

class ScalarBuilder(Enum):

    @staticmethod
    def build(value: int) -> Result[Scalar]:
        try:
            candidate = Scalar(value)
            result = ScalarValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(ScalarBuilder, result)
            return result
        except Exception as e:
            return Result(payload=None, exception=e)
