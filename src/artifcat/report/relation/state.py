# src/artifact/report/relation/state.py

"""
Module: artfifact.report.relation.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto

class RelationState(Enum):
    NO_RELATION = auto(),
    BIDIRECTIONAL = auto(),
    STALE_LINK_NOT_PURGED = auto(),
    REGISTRATION_NOT_SUBMITTED = auto(),


