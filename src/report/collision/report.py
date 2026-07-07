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

from blueprint import Blueprint
from report import CollisionState, Report


@dataclass
class CollisionReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents the results of a attribute collision tests.
    
    Attributes:
        target_set: Any
        collider: Any
        collision_value: Any
        exception: Exception
        state: CollisionState
        colliding_variable: Optional[str]
        
        collision_exists: bool
        is_no_collision: bool
        
    Provides:
        
        -   def collision_occurred(
                    colliding_variable: str,
                    collision_value: Any,
                    collider: Any,
                    exception: Exception
            ) -> CollisionReport
            
        -   def no_collision_occurred(
                    colliding_variable: str,
                    collision_value: Any,
                    collider: Any,
                    exception: Exception
            ) -> CollisionReport[Any]

    Super Class:
        Report
    """
    state: CollisionState
    collider: Optional[Any]
    target_set: Optional[Blueprint]
    collision_value: Optional[Any]
    colliding_variable: Optional[str]
    exception: Optional[Exception]

    @property
    def collision_exists(self) -> bool:
        return not self.is_no_collisions
    
    @property
    def is_no_collisions(self) -> bool:
        return (
                not self._collider_found() and
                self.state == CollisionState.NO_COLLISIONS
        )
    
    def _collider_found(self) -> bool:
        return (
                self.colliding_variable is not None and
                self.collision_value is not None and
                self.target_set is not None and
                self.collider is not None and
                self.exception is not None
        )
    
    @classmethod
    def collision(
            cls,
            target_set: Blueprint,
            colliding_variable: str,
            collision_value: Any,
            collider: Any,
            exception: Exception
    ) -> CollisionReport:
        return cls(
            collider=collider,
            exception=exception,
            target_set=target_set,
            collision_value=collision_value,
            colliding_variable=colliding_variable,
            state=CollisionState.COLLISION_DETECTED,
        )
    
    @classmethod
    def no_collisions(cls, target_set: Blueprint) -> CollisionReport:
        return cls(
            target_set=target_set,
            state=CollisionState.NO_COLLISIONS,
        )
    