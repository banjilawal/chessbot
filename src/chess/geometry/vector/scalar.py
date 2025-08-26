from chess.common.config import BOARD_DIMENSION
from chess.exception.null.number import NullNumberException
from chess.exception.offset.mul import NegativeScalarException, ZeroScalarException, ScalarOutofBoundsException


class Scalar:
    _value: int

    def __init__(self, value: int):
        method = "Scalar.__init__()"
        if value is None:
            raise NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")

        if value < 0:
            raise NegativeScalarException(f"{method}: {NegativeScalarException.DEFAULT_MESSAGE}")

        if value == 0:
            raise ZeroScalarException(f"{method}: {ZeroScalarException.DEFAULT_MESSAGE}")

        if value >= BOARD_DIMENSION:
            raise ScalarOutofBoundsException(
                f"{method}: scalar {ScalarOutofBoundsException.DEFAULT_MESSAGE}"
            )
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Scalar):
            return False

        return self._value == other.value


    def __hash__(self):
        return hash(self._value)


    def __str__(self):
        return f"Scalar(value={self._value})"