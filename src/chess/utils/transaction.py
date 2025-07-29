from chess.utils.operation_result import OperationResult


class Transaction:
    _id: int
    _result: OperationResult
    _message: str

    def __init__(self, transaction_id: int, result: OperationResult, message: str):
        self._id = transaction_id
        self._result = result
        self._message = message

    @property
    def id(self) -> int:
        return self._id

    @property
    def get_result(self) -> OperationResult:
        return self._result

    @property
    def get_message(self) -> str:
        return self._message