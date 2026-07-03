# src/logic/promotion/event/build/exception.py

"""
Module: logic.promotion.event.build.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""



from system import BuilderException
from logic.promotion import PromotionEventException


class PromotionEventBuilderException(PromotionEventException, BuilderException):
    ERR_CODE = "PROMOTION_EVENT_EXCEPTION"
    MSG = "PromotionEvent raised an exception."