# src/chess/square/service/menu/build/request/validator/validator.py

"""
Module: chess.square.service.menu.build.request.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any

from chess.square import ServiceRequest, SquareBuildOperation
from chess.system import LoggingLevelRouter, Validator


class BuildSquareRequestValidator(Validator[SquareBuildOperation]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            operation: SquareBuildOperation
    ) -> Validator[SquareBuildOperation]:
    