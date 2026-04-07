# src/model/report/collision/report.py

"""
Module: model.report.collision.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Generic, Optional, TypeVar

from model import CollisionState

T = TypeVar("T")


class CollisionReport(Generic[T]):
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
    _collider: Optional[T]
    _state: CollisionState
    _exception: Optional[Exception]


    def __init__(
            self,
            state: CollisionState,
            colliding_variable: Optional[str] = None,
            target: Optional[T] = None,
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
        self._target = target
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
    def target(self) -> T:
        return self._target
    
    @property
    def collider(self) -> Optional[T]:
        return self._collider
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def collision_exists(self) -> bool:
        return (
                self.colliding_variable is not None and
                self.collision_value is not None and
                self.target is not None and
                self._collider is not None and
                self.exception is not None and
                self.state == CollisionState.COLLISION_DETECTED
        )
    
    @property
    def is_no_collision(self) -> bool:
        return (
                self.colliding_variable is None and
                self.collision_value is None and
                self.target is  None and
                self._collider is None and
                self.exception is None and
                self.state == CollisionState.NO_COLLISIONS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.colliding_variable is None and
                self.collision_value is None and
                self.target is None and
                self._collider is None and
                self.exception is not None and
                self.state == (
                        CollisionState.DETECTOR_FAILED or
                        CollisionState.DETECTOR_TIMED_OUT
                )
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.colliding_variable is None and
                self.collision_value is None and
                self._collider is None and
                self.target is None and
                self.exception is not None and
                self.state == CollisionState.DETECTOR_TIMED_OUT
        )
    
    @classmethod
    def collision_occurred(
            cls,
            colliding_variable: str,
            val: Any,
            target: T,
            collider: T,
            exception: Exception
    ) -> CollisionReport[T]:
        return cls(
            colliding_variable=colliding_variable,
            collision_value=val,
            target=target,
            collider=collider,
            exception=exception,
            state=CollisionState.COLLISION_DETECTED,
        )
    
    @classmethod
    def no_collision(cls) -> CollisionReport[T]:
        return cls(
            colliding_variable=None,
            collision_value=None,
            target=None,
            collider=None,
            exception=None,
            state=CollisionState.NO_COLLISIONS,
        )
    
    @classmethod
    def failure(cls, exception: Exception):
        return cls(
            colliding_variable=None,
            collision_value=None,
            target=None,
            collider=None,
            exception=exception,
            state=CollisionState.DETECTOR_FAILED,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception):
        return cls(
            colliding_variable=None,
            collision_value=None,
            target=None,
            collider=None,
            exception=exception,
            state=CollisionState.DETECTOR_TIMED_OUT,
        )
    