# src/chess/square/service/menu/operation/validator/validator.py

"""
Module: chess.square.service.menu.operation.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.square import ServiceOperation, Validator


class ServiceOperationValidator(Validator[ServiceOperation], ABC):
    pass