# src/chess/promotion/event/exception.py

"""
Module: chess.promotion.event.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from chess.system import EventException

__all__ = [
    "PromotionEventException",
]

class PromotionEventException(EventException):
    ERROR_CODE = "PROMOTION_EVENT_ERROR"
    DEFAULT_MESSAGE = "PromotionEvent raised an exception."