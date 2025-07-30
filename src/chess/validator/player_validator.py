
from chess.player.player import Player
from chess.transaction.failure import Failure
from chess.transaction.status_code import StatusCode
from chess.transaction.transaction_result import TransactionResult


class PlayerValidator:

    @staticmethod
    def is_not_null(self, player: Player) -> TransactionResult:
        method = "PlayerValidator.is_not_null"

        if player is None:
            return TransactionResult(method, Failure(f"{player} is null"))
        return TransactionResult(method, StatusCode.SUCCESS)