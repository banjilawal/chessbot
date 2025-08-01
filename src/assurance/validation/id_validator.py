from chess.transaction.transaction_result import TransactionResult, Failure, StatusCode



class IdValidator:

    @staticmethod
    def id_is_positive(id: int) -> TransactionResult:
        method = "IdValidator.id_is_positive"
        if id < 1:
            return TransactionResult(method, Failure(f"Id {id} is not positive."))
        return TransactionResult(method, StatusCode.SUCCESS)

    @staticmethod
    def id_exists(id: int) -> TransactionResult:
        method = "IdValidator.id_exists"
        if id is None:
            return TransactionResult(method, Failure(f"{id} must exist"))
        return TransactionResult(method, StatusCode.SUCCESS)
