# src/logic/promotion/event/exception.py

"""
Module: logic.promotion.event.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from logic.system import EventException

__all__ = [
    "PromotionEventException",
]

class PromotionEventException(EventException):
    ERR_CODE = "PROMOTION_EVENT_EXCEPTION"
    MSG = "PromotionEvent raised an exception."