# src/logic/promotion/event/validator/exception/null/__init__.py

"""
Module: logic.promotion.event.validator.exception.null.__init__
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from logic.system import NullException
from logic.promotion import InvalidPromotionEventException

class NullPromotionEventException(
    InvalidPromotionEventException,
    NullException
):
    ERROR_MSG = "NULL_PROMOTION_EVENT_EXCEPTION"
    MSG = "PromotionEvent cannot be null."