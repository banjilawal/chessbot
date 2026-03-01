# src/logic/promotion/event/builder/exception.py

"""
Module: logic.promotion.event.builder.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""



from logic.system import BuildException
from logic.promotion import PromotionEventException


class PromotionEventBuildException(PromotionEventException, BuildException):
    ERR_CODE = "PROMOTION_EVENT_EXCEPTION"
    MSG = "PromotionEvent raised an exception."