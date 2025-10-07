# src/chess/event/promotion/exception.py

"""
Module: `chess.event.promotion.exception`
Author: Banji Lawal
Created: 2025-10-05
version: 1.0.0

Provides: 
Holds exceptions belonging to promotion handling objects.

Contains:
See the list of exception in the `__alL__` list following
"""

from chess.event import EventException, TransactionException
from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'PromotionEventException',

#====================== PROMOTION_EVENT VALIDATION EXCEPTIONS ======================# 
  'NullPromotionEventException',
  'InvalidPromotionEventException',

#====================== PROMOTION_EVENT BUILD EXCEPTIONS ======================# 
  'PromotionEventBuildFailed',

#====================== PROMOTION_TRANSACTION EXCEPTIONS ======================# 
  'PromotionTransactionException',
  'NullPromotionTransactionException',
]

class PromotionEventException(ChessException):
  """
  Super class of exceptions organic to `PromotionEven` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `PromotionEventException` exists primarily to allow catching all `PromotionEven`
  exceptions.
  """
  ERROR_CODE = "PROMOTION_EVENT_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent raised an exception."


#======================#  PROMOTION_EVENT VALIDATION EXCEPTIONS ======================# 
class NullPromotionEventException(PromotionEventException, NullException):
  """Raised if an entity, method, or operation requires a `PromotionEvent` but gets null instead."""
  pass

class InvalidPromotionEventException(PromotionEventException, ValidationException):
  """
  Raised by PromotionEventValidator if a client fails sanity checks. Exists to catch all
  exceptions raised validating an existing `PromotionEvent` candidate.
  """
  ERROR_CODE = "PROMOTION_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent validation failed."


#======================#  PROMOTION_EVENT BUILD EXCEPTIONS ======================# 
class PromotionEventBuildFailed(PromotionEventException, BuildFailedException):
  """
  Raised when `PromotionEventBuilder` crashed while building a new `PromotionEven`. Exists
  primarily to catch all exceptions raised creating `PromotionEvent` objects.
  """
  ERROR_CODE = "PROMOTION_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent build failed."


#======================#  PROMOTION_TRANSACTION EXCEPTIONS ======================# 
class PromotionTransactionException(TransactionException):
  """
  Wraps any errors raised during the promotion's lifecycle.
  """
  ERROR_CODE = "PROMOTION_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "PromotionTransaction raised an exception."

class NullPromotionTransactionException(TransactionException):
  """Raised if an entity, method, or operation requires a `PromotionEvent` but gets null instead."""
  ERROR_CODE = "PROMOTION_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "PromotionTransaction raised an exception."
