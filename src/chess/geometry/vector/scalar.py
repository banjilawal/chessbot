from chess.common.config import BOARD_DIMENSION
from chess.exception.null.number import NullNumberException
from chess.exception.offset.mul import ScalarBelowLowerBoundException, ZeroScalarException, ScalarAboveUpperBoundException


class Scalar:
    _value: int

    def __init__(self, value: int):
        method = "Scalar.__init__()"
        if value is None:
            raise NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")

        if value <= -BOARD_DIMENSION:
            raise ScalarBelowLowerBoundException(f"{method}: {ScalarBelowLowerBoundException.DEFAULT_MESSAGE}")

        if value >= BOARD_DIMENSION:
            raise ScalarAboveUpperBoundException(
                f"{method}: scalar {ScalarAboveUpperBoundException.DEFAULT_MESSAGE}"
            )
        #
        # if value == 0:
        #     raise ZeroScalarException(f"{method}: {ZeroScalarException.DEFAULT_MESSAGE}")


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