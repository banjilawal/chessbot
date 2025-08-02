from enum import Enum, auto

from assurance.result import Result


class StatusCode(Enum):
    LOADING = auto()
    SUCCESS = auto()
    FAILURE = auto()


class TransactionReport:
    _method_name: str
    _status_code: StatusCode
    _operation_result: Result

    def __init__(self, method_name: str, status_code: StatusCode, operation_result: Result):
        self._method_name = method_name
        self._status_code = status_code
        self._operation_result = operation_result


    @property
    def method_name(self) -> str:
        return self._method_name


    @property
    def status_code(self) -> StatusCode:
        return self._status_code


    @property
    def operation_result(self) -> Result:
        return self._operation_result

