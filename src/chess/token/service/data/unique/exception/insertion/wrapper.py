from chess.system import InsertionFailedException


class UniqueTokenInsertionFailedException(InsertionFailedException):
    ERROR_CODE = "UNIQUE_TOKEN_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Unique token insertion failed."