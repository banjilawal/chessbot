# src/logic/token/service/operation/mate/exception.py

"""
Module: logic.token.service.operation.mate.operation
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from system import Builder, BuildResult, LoggingLevelRouter
from model.token import Checkmate, KingToken


class BuildCheckmate(Builder[Checkmate]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            king: KingToken,
    ) -> BuildResult[Checkmate]:
        pass