# src/chess/system/transaction/transaction.py

"""
Module: chess.system.transaction.transaction
Author: Banji Lawal
Created: 2025-08-11
Updated: 2025-10-10
"""

from typing import TypeVar
from abc import ABC, abstractmethod
from chess.system import LoggingLevelRouter, TransactionResult, TransactionState

T = TypeVar("T", bound='Event')


class Transaction(ABC, [T]):
  """"""
  _event: T
  _state: TransactionState

  @LoggingLevelRouter.monitor
  def __init__(self, event: T):
    self._event = event
    self._state = TransactionState.RUNNING

  @property
  def event(self) -> T:
    return self._event


  @property
  def state(self) -> TransactionState:
    return self._state


  @abstractmethod
  @LoggingLevelRouter.monitor
  def execute(self) -> TransactionResult:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not null.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`int`): the visitor_id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    pass
