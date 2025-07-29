from dataclasses import dataclass
from os.path import defpath
from typing import Union

from chess.transaction.failure import Failure
from chess.transaction.status_code import StatusCode


@dataclass(Frozen=True)
class TransactionResult:
    _id: int
    _method_name: str
    _status: StatusCode
    _outcome: Union[StatusCode, Failure]

    @property
    def id(self) -> int:
        return self._id

    @property
    def method_name(self) -> str:
        return self._method_name

    @property
    def status(self) -> StatusCode:
        return self._status

    @property
    def is_success(self) -> bool:
        return self._status == StatusCode.SUCCESS

    @property
    def is_failure(self) -> bool:
        return isinstance(self._outcome, Failure)
