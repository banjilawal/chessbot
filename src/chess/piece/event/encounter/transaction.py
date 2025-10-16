"""
Module: transaction
Author: Banji Lawal
Created: 2025-10-01

Purpose:
  Implements the `ScanTransaction` class, responsible for managing the creation and recording of
  team `Discovery` inside team `Square` by an actor.

Contents:
  - `ScanTransaction:` Main class responsible for executing event directives.

Notes:
  This module is part of the chess.event.event.encounter package.
  Exceptions raised during execution are defined in err.py and err.py.
"""

from typing import cast

from chess.piece import Discovery, DiscoveryBuilder
from chess.system import ExecutionContext, TransactionResult
from chess.piece.discover.exception import AddingValidDiscoveryFailedException
from chess.event import (
  ScanEvent, OccupationTransaction, ScanTransactionException, OccupationEventException, ScanEventValidator
)

class ScanTransaction(OccupationTransaction[ScanEvent]):

  @staticmethod
  def execute(event: ScanEvent, context: ExecutionContext) -> TransactionResult:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not null.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`int`): the id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `exception` (`Exception`) - An exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    method = "ScanTransaction.execute"

    try:
      validation = ScanEventValidator.validate(event, context)
      if not validation.is_success():
        return TransactionResult(event, exception=validation.exception)

      build_result = DiscoveryBuilder.build(observer=event.observer, subject=event.subject)
      if not build_result.is_success():
        return TransactionResult(event, exception=build_result.exception)

      discovery = cast(Discovery, build_result.payload)
      if discovery not in event.observer.discoveries:
        event.observer.discoveries.record_discovery(discovery=discovery)

      if discovery not in event.observer.discoveries.items:
        return TransactionResult(
          event=event,
          exception=AddingValidDiscoveryFailedException(
            f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"
          )
        )

      return TransactionResult(event=event)
    except ScanTransactionException as e:
      raise ScanTransactionException(f"{method}: {e.message}") from e

    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise ScanTransactionException(f"{method}: {e}") from e