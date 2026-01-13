from chess.system import InsertionFailedException


class TokenInsertionFailedException(InsertionFailedException):
    ERROR_CODE = "TOKEN_INSERTION_FAILURE"
    DESCRIPTION = "Token insertion failed."