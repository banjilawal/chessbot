from assurance.transaction_report import StatusCode


class Failure:
    _code: StatusCode
    _message: str

    def __init__(self, message: str="Operation failed"):
        self._code = StatusCode.FAILURE
        self._message = message

    @property
    def code(self) -> StatusCode:
        return self._code

    @property
    def message(self) -> str:
        return self._message

    def is_failure(self) -> bool:
        return self._code == StatusCode.FAILURE


