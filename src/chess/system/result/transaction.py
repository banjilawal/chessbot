from typing import Optional

from chess.system import Result
from chess.transaction import Event

class TransactionResult:
    """
    Result of a transaction that changes an entity's state.

    Use factory methods to create instances:
    - TransactionResult.success()
    - TransactionResult.failed()
    - TransactionResult.rolled_back()

    Direct constructor usage is not recommended.
    """

    _event: Event
    _exception: Optional[Exception]
    _was_rolled_back: bool

    def __init__(
        self,
        event: Event,
        exception: Optional[Exception] = None,
        was_rolled_back: bool = False
    ):
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.__init__"

        self._event = event
        self._exception = exception
        self._was_rolled_back = was_rolled_back


    @property
    def event(self) -> Optional[Event]:
        return self._event

    @property
    def exception(self) -> Optional[Exception]:
        return self._exception

    @property
    def was_rolled_back(self) -> bool:
        return self._was_rolled_back

    def is_success(self) -> bool:
        method = f"{self.__class__.__name__}.is_success"
        """True if transaction success condition was true after the state change"""

        return self._exception is None and not self._was_rolled_back

    #
    # def is_processing(self) -> bool:
    #     method = f"{self.__class__.__name__}.is_processing"
    #     """True if transaction still processing, has not changed state"""
    #
    #     return self._event is None and self._exception is None and not self._was_rolled_back
    #
    #
    # def is_failed(self) -> bool:
    #     method = f"{self.__class__.__name__}.is_failed"
    #     """True if raised an team_exception before the state changed"""
    #
    #     return not (self._exception  is None and self._was_rolled_back)
    #
    #
    # @classmethod
    # def success(cls, outcome_id: int, request: Action, event: Event) -> 'TransactionResult':
    #     method = f"{cls.__class__.__name__}.success"
    #     """Create a successful outcome"""
    #
    #     return cls(
    #         op_result_id=outcome_id,
    #         request=request,
    #         event=event,
    #         err=None,
    #         was_rolled_back=False
    #     )
    #
    #
    # @classmethod
    # def processing(cls, outcome_id: int, request: Action) -> 'TransactionResult':
    #     method = f"{cls.__class__.__name__}.processing"
    #
    #     """Create a processing outcome"""
    #     return cls(
    #         op_result_id=outcome_id,
    #         request=request,
    #         event=None,
    #         err=None,
    #         was_rolled_back=False
    #     )
    #
    #
    # @classmethod
    # def failed(cls, outcome_id: int, request: Action, err: Exception) -> 'TransactionResult':
    #     method = f"{cls.__class__.__name__}.failed"
    #     """Create a failed outcome"""
    #
    #     return cls(
    #         op_result_id=outcome_id,
    #         request=request,
    #         event=None,
    #         err=err,
    #         was_rolled_back=False
    #     )
    #
    #
    # @classmethod
    # def roll_back(cls, outcome_id: int, request: Action, event: Event) -> 'TransactionResult':
    #     method = f"{cls.__class__.__name__}.rolled_back"
    #     """Create a rolled back outcome"""
    #
    #     return cls(
    #         op_result_id=outcome_id,
    #         request=request,
    #         event=event,
    #         err=None,
    #         was_rolled_back=True
    #     )





