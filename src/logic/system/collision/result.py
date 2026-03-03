# src/logic/system/collision/result.py

"""
Module: logic.system.collision.result
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Generic, Optional, TypeVar

from logic.system import CollisionStatus

T = TypeVar("T")


class CollisionDetectionResult(Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a collision to the caller.
    2.  Enforcing mutual exclusion. A CollisionDetectionResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (DataResultEnum)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    _var: Optional[str]
    _value: Optional[Any]
    _target: Optional[T]
    _collider: Optional[T]
    _state: CollisionStatus
    _exception: Optional[Exception]


    def __init__(
            self,
            state: CollisionStatus,
            var: Optional[str] = None,
            target: Optional[T] = None,
            value: Optional[Any] = None,
            collider: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        super().__init__(state=state, target=target, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "CollisionDetectionResult.result"
        self._var = var
        self._value = value
        self._state = state
        self._target = target
        self._collider = collider
        self._exception = exception
        
    @property
    def state(self) -> CollisionStatus:
        return self._state
    
    @property
    def var(self) -> Optional[str]:
        return self._var
    
    @property
    def value(self) -> Optional[Any]:
        return self._value
        
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
                self.var is not None and
                self.value is not None and
                self.target is not None and
                self._collider is not None and
                self.exception is not None and
                self.state == CollisionStatus.COLLISION_DETECTED
        )
    
    @property
    def is_no_collision(self) -> bool:
        return (
                self.var is None and
                self.value is None and
                self.target is  None and
                self._collider is None and
                self.exception is None and
                self.state == CollisionStatus.NO_COLLISIONS
        )
    
    @property
    def is_analyzer_failure(self) -> bool:
        return (
                self.var is None and
                self.value is None and
                self.target is None and
                self._collider is None and
                self.exception is not None and
                self.state == (
                        CollisionStatus.DETECTOR_FAILED or
                        CollisionStatus.DETECTOR_TIMED_OUT
                )
        )
    
    @property
    def is_analyzer_timed_out(self) -> bool:
        return (
                self.var is None and
                self.value is None and
                self._collider is None and
                self.target is None and
                self.exception is not None and
                self.state == CollisionStatus.DETECTOR_TIMED_OUT
        )
    
    @classmethod
    def collision(
            cls,
            var: str,
            val: Any,
            target: T,
            collider: T,
            exception: Exception
    ) -> CollisionDetectionResult[T]:
        return cls(
            var=var,
            value=val,
            target=target,
            collider=collider,
            exception=exception,
            state=CollisionStatus.COLLISION_DETECTED,
        )
    
    @classmethod
    def no_collision(cls) -> CollisionDetectionResult[T]:
        return cls(
            var=None,
            value=None,
            target=None,
            collider=None,
            exception=None,
            state=CollisionStatus.NO_COLLISIONS,
        )
    
    @classmethod
    def detector_failure(cls, exception: Exception):
        return cls(
            var=None,
            value=None,
            target=None,
            collider=None,
            exception=exception,
            state=CollisionStatus.DETECTOR_FAILED,
        )
    
    @classmethod
    def detector_timed_out(cls, exception: Exception):
        return cls(
            var=None,
            value=None,
            target=None,
            collider=None,
            exception=exception,
            state=CollisionStatus.DETECTOR_TIMED_OUT,
        )
    