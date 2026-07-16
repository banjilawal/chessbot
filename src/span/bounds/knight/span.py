# src/span/bounds/knight/span.py

"""
Module: span.bounds.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Knight, Vector
from span import KnightDeltaVectors, SpanBounds


class KnightSpanBounds(SpanBounds[Knight]):
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfBounds errors by calculating the last point in the direction
            of travel

    Attributes:

    Provides:

    Super Class:
        SpanBounds
    """
    def __init__(self, origin: Vector, delta_vectors: KnightDeltaVectors):
        super().__init__(origin=origin, delta_vectors=delta_vectors)
