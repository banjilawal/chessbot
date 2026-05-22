# src/report/collision/report.py

"""
Module: report.collision.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from report import CollisionState

@dataclass
class CollisionReport:
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents the results of a attribute collision tests.
    
    Attributes:
        collider: T
        collision_value: Any
        exception: Exception
        state: CollisionState
        colliding_variable: Optional[str]
        
    Provides:
        -   def collision_exists() -> bool
        -   def is_no_collision() -> bool
        
        -   def collision_occurred(
                    colliding_variable: str,
                    collision_value: Any,
                    collider: Any,
                    exception: Exception
            ) -> CollisionReport[Any]

    Super Class:
        Report
    """
    colliding_variable: Optional[str]
    collision_value: Optional[Any]
    collider: Optional[Any]
    state: CollisionState
    exception: Optional[Exception]

    
    @property
    def collision_exists(self) -> bool:
        return (
                self.colliding_variable is not None and
                self.collision_value is not None and
                self.collider is not None and
                self.exception is not None and
                self.state == CollisionState.COLLISION_DETECTED
        )
    
    @property
    def is_no_collision(self) -> bool:
        return (
                self.colliding_variable is None and
                self.collision_value is None and
                self._collider is None and
                self.exception is None and
                self.state == CollisionState.NO_COLLISIONS
        )
    
    @classmethod
    def collision_occurred(
            cls,
            colliding_variable: str,
            collision_value: Any,
            collider: Any,
            exception: Exception
    ) -> CollisionReport[Any]:
        return cls(
            colliding_variable=colliding_variable,
            collision_value=collision_value,
            collider=collider,
            exception=exception,
            state=CollisionState.COLLISION_DETECTED,
        )
    
    @classmethod
    def no_collision(cls) -> CollisionReport:
        return cls(
            colliding_variable=None,
            collision_value=None,
            collider=None,
            exception=None,
            state=CollisionState.NO_COLLISIONS,
        )
    