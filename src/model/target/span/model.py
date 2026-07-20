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
            root: Vector,
            targets: Optional[VectorSet] | None = None,
    ):
        """
        Args:
            root: Vector
            targets: Optional[VectorSet]
        """
        super().__init__(root=root, targets=targets)

    def remove_root_from_targets(self) -> TargetVectorSet:
        if self.root_is_not_target:
            return self
        return cast(
            TargetSpanSet,
            super().remove_root_from_targets()
        )
        

        