from enum import Enum

from chess.exception import NullNumberException
from chess.scalar import Scalar, ScalarAboveBoundsException, ScalarBelowBoundsException, ScalarBuilderException
from chess.common import BuildResult, BOARD_DIMENSION
from assurance import ThrowHelper

class ScalarBuilder(Enum):

    @staticmethod
    def build(value: int) -> BuildResult[Scalar]:

        method = "ScalarBuilder.build"
        try:
            if value is None:
                ThrowHelper.throw_if_invalid(
                    ScalarBuilder, NullNumberException(NullNumberException.DEFAULT_MESSAGE)
                )
            if value < -BOARD_DIMENSION:
                ThrowHelper.throw_if_invalid(
                    ScalarBuilder, ScalarBelowBoundsException(ScalarBelowBoundsException.DEFAULT_MESSAGE)
                )
            if value > BOARD_DIMENSION:
                ThrowHelper.throw_if_invalid(
                    ScalarBuilder, ScalarAboveBoundsException(ScalarAboveBoundsException.DEFAULT_MESSAGE)
            )

            return BuildResult(payload=Scalar(value=value))

        except Exception as e:
            raise ScalarBuilderException(f"{method}: {ScalarBuilderException.DEFAULT_MESSAGE}") from e
