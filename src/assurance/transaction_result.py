from enum import Enum, auto

from assurance.result import Result


class StatusCode(Enum):
    LOADING = auto()
    SUCCESS = auto()
    FAILURE = auto()


class TransactionResult:
    _transaction_method_name: str
    _status_code: StatusCode
    _outcome: Result

    def __init__(self, transaction_method_name: str, status_code: StatusCode, outcome: Result):
        self._transaction_method_name = transaction_method_name
        self._status_code = status_code
        self._outcome = outcome


    @property
    def transaction_method_name(self) -> str:
        return self._transaction_method_name


    @property
    def status_code(self) -> StatusCode:
        return self._status_code


    @property
    def outcome(self) -> Result:
        return self._outcome

