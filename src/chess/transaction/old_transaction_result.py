from typing import Union
from chess.transaction.status_code import StatusCode
from chess.transaction.failure import Failure

class OldTransactionResult:
    _method_name: str
    _outcome: Union[StatusCode, Failure]

    def __init__(self, method_name: str, outcome: Union[StatusCode, Failure]):
        self._method_name = method_name
        self._outcome = outcome

    @property
    def method_name(self) -> str:
        return self._method_name

    @property
    def outcome(self) -> Union[StatusCode, Failure]:
        return self._outcome

    @property
    def status(self) -> StatusCode:
        return StatusCode.FAILURE if isinstance(self._outcome, Failure) else self._outcome

    @property
    def is_success(self) -> bool:
        return self.status == StatusCode.SUCCESS

    @property
    def is_failure(self) -> bool:
        return self.status == StatusCode.FAILURE

