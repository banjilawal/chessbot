# src/chess/system/collection/operation/collision/result.py

"""
Module: chess.system.collection.operation.collision.result
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from chess.system import CollisionResultEnum, CollisionResultState, DataResult, MethodNotImplementedException

T = TypeVar("T")

class CollisionReport(DataResult[T], Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a collision to the caller.
    2.  Enforcing mutual exclusion. A CollisionReport can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (DataResultEnum)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    _collision: Optional[T]

    def __init__(
            self,
            target: T,
            state: CollisionResultState,
            exception: Optional[Exception] = None,
            collider: Optional[T] = None,
    ):
        super().__init__(state=state, payload=target, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "CollisionReport.result"
        self._collider = collider
        
    @property
    def target(self) -> T:
        return self.payload
    
    @property
    def collider(self) -> Optional[T]:
        return self._collider
    
    @property
    def is_success(self) -> bool:
        return (
                self._collider is not None and
                self.target is not None and
                self.exception is None and
                self.state == CollisionResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self._collider is None and
                self.target is not None and
                self.exception is not None and
                self.state == CollisionResultEnum.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self._collider is None and
                self.target is not None and
                self.exception is not None and
                self.state == CollisionResultEnum.TIMED_OUT
        )
    
    @classmethod
    def collision_detected(cls, target: T, collider: T,) -> CollisionReport[T]:
        return cls(
            target=target,
            collider=collider,
            exception=None,
            state=CollisionResultState(classification=CollisionResultEnum.COLLISION_DETECTED),
        )
    
    @classmethod
    def no_collision_detected(cls, target: T, ) -> CollisionReport[T]:
        return cls(
            target=target,
            collider=None,
            exception=None,
            state=CollisionResultState(classification=CollisionResultEnum.NO_COLLISIONS),
        )
    
    @classmethod
    def detection_failure(cls, target: T, exception: Exception):
        return cls(
            target=target,
            collider=None,
            exception=exception,
            state=CollisionResultState(classification=CollisionResultEnum.FAILURE),
        )
    
    @classmethod
    def collision_timed_out(cls, target: T, exception: Exception):
        return cls(
            target=target,
            collider=None,
            exception=exception,
            state=CollisionResultState(classification=CollisionResultEnum.TIMED_OUT),
        )
    
    @classmethod
    def success(cls, payload: T) -> CollisionReport[T]:
        return cls.detection_failure(
            target=payload,
            exception=MethodNotImplementedException(
                f"CollisionReport does not support Result.success. Use CollisionReport.collision_detected instead."
            )
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> CollisionReport[T]:
        return cls.detection_failure(
            target=None,
            exception=MethodNotImplementedException(
                ex=exception,
                message=(
                    f"CollisionReport does not support Result.failure. "
                    f"Use CollisionReport.collision_failure instead."
                ),
            )
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> CollisionReport[T]:
        return cls.collision_timed_out(
            target=None,
            exception=MethodNotImplementedException(
                ex=exception,
                message=(
                    f"CollisionReport does not support Result.timed_out. "
                    f"Use CollisionReport.collision_timed instead."
                ),
            )
        )