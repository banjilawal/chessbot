from chess.system import DeletionFailedException


class UniqueTokenDeletionFailedException(DeletionFailedException):
    ERROR_CODE = "UNIQUE_TOKEN_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Unique token deletion failed."