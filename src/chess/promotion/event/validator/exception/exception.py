# src/chess/promotion/event/number_bounds_validator/exception/exception.py

"""
Module: chess.promotion.event.number_bounds_validator.exception.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


__all__ = [
    "InvalidPromotionEventException",
]


from chess.system import ValidationException
from chess.promotion import PromotionEventException


class InvalidPromotionEventException(PromotionEventException, ValidationException):
    """
    Raised by PromotionEventValidator if team_name client fails sanity checks. Exists to catch all
    exception raised validating an existing `PromotionEvent` candidate.
    """
    ERROR_CODE = "PROMOTION_EVENT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PromotionEvent validation failed."