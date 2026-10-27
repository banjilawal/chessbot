#  src/domain/bluprint/context__init__.py

"""
Module: domain.bluprint.context.__init__
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class FlagState(Enum):
    NO_FLAGS = auto(),
    TOO_MANY_FLAGS = auto(),
    VALID_SIZE = auto(),
    UNKNOWN = auto(),
    