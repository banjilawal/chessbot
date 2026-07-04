# src/logic/snapshot/service/validator.py

"""
Module: logic.snapshot.service.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from system import QueryService
from model.state.game import SnapshotContext


class SnapshotQueryService(QueryService[SnapshotContext]):
    pass
