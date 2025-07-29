from dataclasses import dataclass

from chess.utils.status_code import StatusCode


@dataclass(Frozen=True)
class TransactionResult:
    code: StatusCode = StatusCode.FAILURE
    message: str = ""


    def is_success(self) -> bool:
        return