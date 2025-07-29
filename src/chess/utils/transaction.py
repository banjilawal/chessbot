from chess.utils.status_code import StatusCode


FailueResult:
    meesage: str

class Transaction:
    _id: int
    _method_name: str
    _result: StatusCode
    _message: str

class Transaction:
    _id: int
    _result: StatusCode
    _message: str

    def __init__(self, transaction_id: int, result: StatusCode, message: str):
        self._id = transaction_id
        self._result = result
        self._message = message

    @property
    def id(self) -> int:
        return self._id

Thhen some sort of transaction(id, mehtod_name: str, succes_condition: bool) -> TransactionResult

    @property
    def get_result(self) -> StatusCode:
        return self._result

    @property
    def get_message(self) -> str:
        return self._message