# src/chess/system/service/menu/execution/validator/validator.py

"""
Module: chess.system.service.menu.execution.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.system import ServiceExecution, Validator


class ServiceExecutionValidator(Validator[ServiceExecution], ABC):
    pass