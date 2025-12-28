# src/chess/system/relation/status.py

"""
Module: chess.system.relation.status
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from enum import Enum


class RelationStatus(Enum):
    NO_RELATION = (),
    BIDIRECTIONAL = (),
    REGISTRATION_NOT_SUBMITTED = (),
