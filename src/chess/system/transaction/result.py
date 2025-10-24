# src/chess/system/travel/old_transaction.py

"""
Module: `chess.system.travel.notification`
Author: Banji Lawal
Created: 2025-09-28
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` reliability requirement.
  2. A satisfaction of the performance requirement.

# SECTION 2 - Scope:
The module covers `Transaction` instances that emit a `TransactionResult` and consumers of the notification.

# SECTION 3 - Limitations:
  1. The module is limited to presenting the answer from a `Search` service provider to the client delivering a query.
  2. The module does not guarantee the accuracy or precision of data in the notification.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. A consistent interface aiding discoverability, understanding and simplicity.

# SECTION 5 - Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.
  2. Performance does not degrade under high old_search loads.

# 6 Feature Delivery Mechanism:
  1. The module implements logic for carrying either an rollback_exception or notification of a successful old_search. in the same
      container. This improves square.
  2. Delivering an rollback_exception in the return instead of raising gives application higher reliability, uptimes and
      survivability.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `Result`

* From Python `typing` Library:
    `Generic`, `TypeVar`, `Optional`

# SECTION 8 - Contains:
1. `SearchResult`
"""

from typing import Optional, cast

from chess.system import Event, NotImplementedException, Result, RollbackException, TransactionState, TransactionResult


class TransactionResult(Result[Event]):
    """
    # ROLE: Builder implementation
  
    # RESPONSIBILITIES:
    1. Process and validate parameters for creating `Team` instances.
    2. Create new `Team` objects if parameters meet specifications.
    2. Report errors and return `BuildResult` with error details.
  
    # PROVIDES:
    `BuildResult`: Return type containing the built `Team` or error information.
  
    # ATTRIBUTES:
    None
    """
    """
    Result of team notification that changes an entity's state.
  
    Use factory methods to create instances:
    - TransactionResult.success()
    - TransactionResult.failed()
    - TransactionResult.rolled_back()
  
    Direct constructor usage is not recommended.
    """
    
    _event_update: Event
    _transaction_state: TransactionState
    _exception: Optional[Exception]
    
    def __init__(
        self,
        event_update: Event,
        transaction_state: TransactionState,
        exception: Optional[Exception] = None
    ):
        super().__init__(payload=event_update, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.__init__"
        self._transaction_state = transaction_state
    
    @property
    def event_update(self) -> Event:
        return cast(Event, self.payload)
    
    @property
    def transaction_state(self) -> Optional[TransactionState]:
        return self._transaction_state
    
    def is_success(self) -> bool:
        return (
            self.exception is None and self.payload is not None and
            self._transaction_state == TransactionState.SUCCESS
        )
    
    def is_failure(self) -> bool:
        return (
            self.exception is not None and
            self._transaction_state == TransactionState.FAILURE or
            self._transaction_state == TransactionState.ROLLED_BACK
        )
    
    def is_rolled_back(self) -> bool:
        return self.exception is not None and self._transaction_state == TransactionState.ROLLED_BACK
    
    def is_timed_out(self) -> bool:
        return self.exception is not None and self._transaction_state == TransactionState.TIMED_OUT
    
    @classmethod
    def success(cls, event_update) -> TransactionResult:
        return cls(event_update, TransactionState.SUCCESS)
    
    @classmethod
    def errored(cls, event_update: Event, exception: Exception) -> TransactionResult:
        return cls(event_update, TransactionState.FAILURE, exception)
    
    @classmethod
    def rolled_back(cls, event_update: Event, rollback_exception: RollbackException) -> TransactionResult:
        return cls(event_update, TransactionState.ROLLED_BACK, rollback_exception)
    
    @classmethod
    def empty(cls) -> Result:
        method = "TransactionResult.empty"
        return Result(
            exception=NotImplementedException(
                f"{method}: {NotImplementedException.DEFAULT_MESSAGE}. TransactionResult must "
                f"always have an event in the payload. It cannot be empty."
            )
        )
