# src/analysis/report/collision/report.py

"""
Module: analysis.report.collision.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from analysis import CollisionState



class CollisionReport:
    """
    Role:Messanger, Data Transport Object, Error Transport Object.

    Responsibilities:
    1.  Send the outcome of a collision to the caller.
    2.  Enforcing mutual exclusion. A CollisionReport can either carry payload or exception. Not both.

    Super Class:
        *   DataResult

    Provides:

    # LOCAL ATTRIBUTES:
        *   state (DataResultEnum)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    _colliding_variable: Optional[str]
    _collision_value: Optional[Any]
    _collider: Optional[Any]
    _state: CollisionState
    _exception: Optional[Exception]


    def __init__(
            self,
            state: CollisionState,
            colliding_variable: Optional[str] = None,
            collision_value: Optional[Any] = None,
            collider: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        super().__init__(state=state, target=target, exception=exception)
        """INTERNAL: Use build methods instead of direct constructor."""
        method = "CollisionReport.result"
        self._colliding_variable = colliding_variable
        self._collision_value = collision_value
        self._state = state
        self._collider = collider
        self._exception = exception
        
    @property
    def state(self) -> CollisionState:
        return self._state
    
    @property
    def colliding_variable(self) -> Optional[str]:
        return self._colliding_variable
    
    @property
    def collision_value(self) -> Optional[Any]:
        return self._collision_value
    
    @property
    def collider(self) -> Optional[Any]:
        return self._collider
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def collision_exists(self) -> bool:
        return (
                self.colliding_variable is not None and
                self.collision_value is not None and
                self._collider is not None and
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
    