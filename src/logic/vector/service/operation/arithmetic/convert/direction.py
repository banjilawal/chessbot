from __future__ import annotations

from enum import Enum, auto


class ConversionDirection(Enum):
    VECTOR_TO_CORD = auto(),
    CORD_TO_VECTOR = auto(),