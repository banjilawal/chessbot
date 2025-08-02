from enum import Enum, auto

from assurance.result import Result


class TransactionReport:
    _method_name: str
    _operation_result: Result

    def __init__(self, method_name: str, operation_result: Result):
        self._method_name = method_name
        self._operation_result = operation_result


    @property
    def method_name(self) -> str:
        return self._method_name


    @property
    def operation_result(self) -> Result:
        return self._operation_result

