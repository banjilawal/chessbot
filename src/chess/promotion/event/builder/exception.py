# src/chess/promotion/event/builder/exception.py

"""
Module: chess.promotion.event.builder.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""



from chess.system import BuildFailedException
from chess.promotion import PromotionEventException


class PromotionEventBuildFailedException(PromotionEventException, BuildFailedException):
    ERROR_CODE = "PROMOTION_EVENT_ERROR"
    DEFAULT_MESSAGE = "PromotionEvent raised an exception."