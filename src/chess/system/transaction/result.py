# src/chess/system/event/transaction.py

"""
Module: `chess.system.event.transaction`
Author: Banji Lawal
Created: 2025-09-28
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` reliability requirement.
  2. A satisfaction of the performance requirement.

# SECTION 2 - Scope:
The module covers `Transaction` instances that emit a `TransactionResult` and consumers of the transaction.

# SECTION 3 - Limitations:
  1. The module is limited to presenting the answer from a `Search` service provider to the client delivering a query.
  2. The module does not guarantee the accuracy or precision of data in the transaction.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. A consistent interface aiding discoverability, understanding and simplicity.

# SECTION 5 - Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.
  2. Performance does not degrade under high old_search loads.

# 6 Feature Delivery Mechanism:
  1. The module implements logic for carrying either an exception or transaction of a successful old_search. in the same
      container. This improves resource.
  2. Delivering an exception in the return instead of raising gives application higher reliability, uptimes and
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

from chess.system import Event, TransactionState, Result


class TransactionResult(Result):
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
  Result of team transaction that changes an entity's state.

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
    """"""
    method = "TransactionResult.is_success"

    return (
      self.exception is None and
      (self.payload is not None and self._transaction_state == TransactionState.SUCCESS)
    )


  def is_failure(self) -> bool:
    """"""
    return (self.exception is not None and
        self._transaction_state == TransactionState.FAILURE or
        self._transaction_state == TransactionState.ROLLED_BACK
    )


  def is_rolled_back(self) -> bool:
    """"""
    return self.exception is not None and self._transaction_state == TransactionState.ROLLED_BACK


  def is_timed_out(self) -> bool:
    return self.exception is not None and self._transaction_state == TransactionState.TIMED_OUT

  #
  # def is_processing(self) -> bool:
  #   method = f"{self.__class__.__name__}.is_processing"
  #   """True if transaction still processing, has not changed state"""
  #
  #   return self._event_update is None and self._exception is None and not self._was_rolled_back
  #
  #
  # def is_failed(self) -> bool:
  #   method = f"{self.__class__.__name__}.is_failed"
  #   """True if raised an exception before the state changed"""
  #
  #   return not (self._exception is None and self._was_rolled_back)
  #
  #
  # @classmethod
  # def success(cls, outcome_id: int, request: Action, event: Event) -> 'TransactionResult':
  #   method = f"{cls.__class__.__name__}.success"
  #   """Create team successful outcome"""
  #
  #   return cls(
  #     op_result_id=outcome_id,
  #     request=request,
  #     event=event,
  #     err=None,
  #     was_rolled_back=False
  #   )
  #
  #
  # @classmethod
  # def processing(cls, outcome_id: int, request: Action) -> 'TransactionResult':
  #   method = f"{cls.__class__.__name__}.processing"
  #
  #   """Create team processing outcome"""
  #   return cls(
  #     op_result_id=outcome_id,
  #     request=request,
  #     event=None,
  #     err=None,
  #     was_rolled_back=False
  #   )
  #
  #
  # @classmethod
  # def failed(cls, outcome_id: int, request: Action, err: Exception) -> 'TransactionResult':
  #   method = f"{cls.__class__.__name__}.failed"
  #   """Create team failed outcome"""
  #
  #   return cls(
  #     op_result_id=outcome_id,
  #     request=request,
  #     event=None,
  #     err=err,
  #     was_rolled_back=False
  #   )
  #
  #
  # @classmethod
  # def roll_back(cls, outcome_id: int, request: Action, event: Event) -> 'TransactionResult':
  #   method = f"{cls.__class__.__name__}.rolled_back"
  #   """Create team rolled back outcome"""
  #
  #   return cls(
  #     op_result_id=outcome_id,
  #     request=request,
  #     event=event,
  #     err=None,
  #     was_rolled_back=True
  #   )





