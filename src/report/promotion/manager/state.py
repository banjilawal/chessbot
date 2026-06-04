# src/report/promotion/manager/state.py

"""
Module: report.promotion.manager.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class PromotionDecision(Enum):
    GRANTED = auto(),
    DENIED = auto(),