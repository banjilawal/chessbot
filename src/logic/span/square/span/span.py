# src/logic/span/square/span.py

"""
Module: logic.span.square.span
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast

from logic.square import Square
from logic.span import Span, SquareRay


class SquareSpan(Span[Square]):
    """
    # ROLE: Data-Holder

    # RESPONSIBILITIES:
    1.  Stores rays projected from a common origin.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Span class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   origin: Square

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See Span class for inherited methods.
    """
    
    def __init__(
            self,
            origin: Square,
            rays: List[SquareRay],
            sub_span_roots: List[Square],
    ):
        super().__init__(origin=origin, rays=rays, sub_span_roots=sub_span_roots)

    @property
    def origin(self) -> Square:
        return cast(Square, self.origin)
    
    @property
    def rays(self) -> List[SquareRay]:
        return cast(List[SquareRay], self.rays)
    
    @property
    def sub_span_roots(self) -> List[Square]:
        return cast(List[Square], self.sub_span_roots)