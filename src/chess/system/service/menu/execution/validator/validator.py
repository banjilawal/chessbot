# src/chess/system/service/menu/operation/validator/validator.py

"""
Module: chess.system.service.menu.operation.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.system import ServiceOperation, Validator


class ServiceOperationValidator(Validator[ServiceOperation], ABC):
    pass