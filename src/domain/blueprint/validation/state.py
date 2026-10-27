# src/domain/bluprint/validation/__init__.py

"""
Module: domain.bluprint.validation.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from enum import Enum, auto

class ValidationState(Enum):
    VALIDATED = auto(),
    NOT_VALIDATED = auto(),
    