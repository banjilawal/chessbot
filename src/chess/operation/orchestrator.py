from abc import abstractmethod, ABC
from typing import Optional

from chess.board.board import Board
from chess.operation.directive import Action


class TransactionOrchestrator(ABC):
    """Orchestrates multiple transactions for complex operations. Routes who does it"""


    def __init__(self):
        self._transactions = {}  # Map command types to transaction handlers

    @staticmethod
    @abstractmethod
    def enter(request: Action, board: Optional[Board]):
        pass


    def register(self, command_type: Type[Command], transaction: Transaction):
        """Register a transaction handler for a command type"""
        self._transactions[command_type] = transaction

    def execute(self, command: Command) -> TransactionOutcome:
        """Execute command using appropriate transaction handler"""
        transaction = self._transactions.get(type(command))
        if not transaction:
            return TransactionOutcome.failed(
                command,
                UnhandledCommandException(f"No handler for {type(command).__name__}")
            )

        return transaction.execute(command)
