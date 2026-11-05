# src/report/collision/collision.py

"""
Module: report.collision.collision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Generic, Optional, TypeVar

from artifcat import CollisionState, Report
from domain import Model

P = TypeVar("P", bound="Model")
A = TypeVar("A")

class CollisionReport(Report, Generic[P, A]):
    """
    Role:
        -   Report

    Responsibilities:
        1.  Capture details about a duplicate attribute collision.

    Attributes:
        state: CollisionState
        match: Optional[A]
        target: Optional[A]
        particle: Optional[P]
        identifier: Optional[str]
        exception:Optional[Exception]
        
        collision_occurred: bool
        no_collision_occurred: bool
        

    Provides:
        -   def no_collision_events() -> CollisionReport
        
        -   def collision_event(
                    match: A,
                    target: A,
                    particle: P,
                    identifier: str,
                    exception: Exception,
            ) -> CollisionReport

    Super Class:
        Report
    """
    _state: CollisionState
    _match: Optional[A]
    _target: Optional[A]
    _particle: Optional[P]
    _identifier: Optional[str]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            state: CollisionState,
            match: Optional[A] | None = None,
            target: Optional[A] | None = None,
            particle: Optional[P] | None = None,
            identifier: Optional[str] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: CollisionState
            match: Optional[A]
            target: Optional[A]
            particle: Optional[P]
            identifier: Optional[str]
            exception:Optional[Exception]
        """
        self._state = state
        self._match = match
        self._target = target
        self._particle = particle
        self._identifier = identifier
        self._exception = exception
        
    @property
    def state(self) -> CollisionState:
        return self._state
        
    @property
    def target(self) -> Optional[A]:
        return self._target
        
    @property
    def match(self) -> Optional[A]:
        return self._match
    
    @property
    def particle(self) -> Optional[P]:
        return self._particle
        
    @property
    def identifier(self) -> Optional[str]:
        return self._identifier
        
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
        
    @property
    def collision_occurred(self) -> bool:
        return (
                self._match is not None and
                self._target is not None and
                self._particle is not None and
                self._identifier is not None and
                self._exception is not None and
                self._state == CollisionState.COLLISION_DETECTED
        )
        
    @property
    def no_collision_occurred(self) -> bool:
        return not self.collision_occurred
    
    @classmethod
    def no_collision_events(cls) -> CollisionReport:
        return cls(state=CollisionState.NO_COLLISIONS)
        
    @classmethod
    def collision_event(
            cls,
            match: A,
            target: A,
            particle: P,
            identifier: str,
            exception: Exception,
    ) -> CollisionReport:
        return cls(
            match=match,
            target=target,
            particle=particle,
            identifier=identifier,
            exception=exception,
            state=CollisionState.COLLISION_DETECTED,
        )