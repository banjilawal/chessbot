# src/logic/token/service/operation/check/process.py

"""
Module: logic.token.service.operation.check.handler
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from logic.system import BuildProcess, BuildResult, LoggingLevelRouter
from logic.token import Check, KingToken


class BuildCheckProcess(BuildProcess[Check]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            king: KingToken,
            token_validator: TokenValidator = TokenValidator(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> BuildResult[Check]:
        pass