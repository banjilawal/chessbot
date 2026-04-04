# src/logic/promotion/event/validation/exception/exception.py

"""
Module: logic.promotion.event.validation.exception.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


__all__ = [
    "InvalidPromotionEventException",
]


from system import ValidationException
from logic.promotion import PromotionEventException


class InvalidPromotionEventException(PromotionEventException, ValidationException):
    """
    Raised by PromotionEventValidator if team_name client fails sanity checks. Exists to catch all
    exception raised validating an existing `PromotionEvent` rank.
    """
    ERR_CODE = "PROMOTION_EVENT_VALIDATION_EXCEPTION"
    MSG = "PromotionEvent validation failed."