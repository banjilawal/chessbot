# src/logic/system/relation/report/state.py

"""
Module: logic.system.relation.report.state
Author: Banji Lawal
Created: 2025-12-28
version: 1.0.0
"""

from enum import Enum, auto

class RelationState(Enum):
    NO_RELATION = auto(),
    BIDIRECTIONAL = auto(),
    STALE_LINK_NOT_PURGED = auto(),
    REGISTRATION_NOT_SUBMITTED = auto(),


