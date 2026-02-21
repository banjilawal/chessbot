from typing import Any, Optional

from chess.system import MethodNotImplementedException
from chess.system.result import Result


class BooleanResult(Result[bool]):
    """"""
    _outcome: bool
    
    def __init__(
            self,
            outcome: Optional[(Any, bool)],
            exception: Optional[Exception] = None
    ):
        super().__init__(payload=outcome, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.__init__"
        self._outcome = outcome
    
    @property
    def is_success(self) -> bool:
        return self.exception is None and self.payload is not None
    
    @property
    def is_failure(self) -> bool:
        return self.exception is not None and self.payload is None
    
    @classmethod
    def success(cls, payload: (Any, bool)) -> BooleanResult:
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> BooleanResult:
        return cls(exception=exception)
    
    @classmethod
    def empty(cls) -> Result:
        method = "TransactionResult.empty"
        return Result(
            exception=MethodNotImplementedException(
                f"{method}: {MethodNotImplementedException.DEFAULT_MESSAGE}. TransactionResult must "
                f"always have an event in the payload. It cannot be empty."
            )
        )