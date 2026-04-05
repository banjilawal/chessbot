# src/logic/token/service/operation/check/exception.py

"""
Module: logic.token.service.operation.check.operation
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from system import Builder, BuildResult, LoggingLevelRouter
from model.token import CheckSquare, KingToken


class BuildCheck(Builder[CheckSquare]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            king: KingToken,
            token_validator: TokenValidator = TokenValidator(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> BuildResult[CheckSquare]:
        pass


5
gZpDCDLCma9oWvaYHBcfzC8ym2X6