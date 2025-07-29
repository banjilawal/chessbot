
from chess.transaction.status_code import StatusCode


class Failure:
    _code: StatusCode = StatusCode.FAILURE
    _message: str = 'Operation failed'

    def __init__(self, code: StatusCode, message: str):
        self._code = code
        self._message = message

    @property
    def code(self) -> StatusCode:
        return self._code

    @property
    def message(self) -> str:
        return self._message

    def is_failure(self) -> bool:
        return self._code == StatusCode.FAILURE


