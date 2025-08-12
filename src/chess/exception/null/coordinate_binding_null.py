from chess.exception.null import NullException


class NullCoordinateBindingException(NullException):
    default_message = f"CoordinateBinding {NullException.default_message}"