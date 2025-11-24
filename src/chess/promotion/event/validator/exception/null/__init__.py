# src/chess/promotion/event/validator/exception/null/__init__.py

"""
Module: chess.promotion.event.validator.exception.null.__init__
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import NullException
from chess.promotion import InvalidPromotionEventException

class NullPromotionEventException(
    InvalidPromotionEventException,
    NullException
):
    ERROR_MESSAGE = "NULL_PROMOTION_EVENT_ERROR"
    DEFAULT_MESSAGE = "PromotionEvent cannot be null."