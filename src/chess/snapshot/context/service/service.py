# src/chess/snapshot/service/service.py

"""
Module: chess.snapshot.service.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextService
from chess.game import SnapshotContext


class SnapshotContextService(ContextService[SnapshotContext]):
    pass
