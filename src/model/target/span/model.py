# src/model/target/span/model.py

"""
Module: model.target.span.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from container import VectorSet
from model import Vector
from model import TargetVectorSet


class TargetSpanSet(TargetVectorSet):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Stores vectors that can be journeyed to from the root.

    Attributes:
        root: Vector
        targets: VectorSet

    Provides:

    Super Class:
        TargetVectorSet
    """
    
    def __init__(
            self,
            hunter: Vector,
            group: Optional[VectorSet] | None = None,
    ):
        """
        Args:
            hunter: Vector
            group: Optional[VectorSet]
        """
        super().__init__(hunter=hunter, group=group)

    def remove_hunter_from_targets(self) -> TargetVectorSet:
        if self.hunter_not_targeting_itself:
            return self
        return cast(
            TargetSpanSet,
            super().remove_hunter_from_targets()
        )
        

        