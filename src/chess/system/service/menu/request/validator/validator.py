# src/chess/system/service/menu/request/validator/validator.py

"""
Module: chess.system.service.menu.request.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.system import ServiceRequest, Validator


class ServiceRequestValidator(Validator[ServiceRequest], ABC):
    pass