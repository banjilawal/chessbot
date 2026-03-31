# src/logic/snapshot/build/exception.py

"""
Module: logic.snapshot.build.build
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.snapshot import Snapshot
from logic.system import BuildResult, Builder



class SnapshotBuilder(Builder[Snapshot]):
    @classmethod
    def build(cls, *args, **kwargs) -> BuildResult[Snapshot]:
        pass