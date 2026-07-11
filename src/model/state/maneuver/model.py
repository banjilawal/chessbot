# src/model/state/model/state/maneuver.py

"""
Module: model.state.model.maneuver
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from model import ManeuverState, Path, StateModel

T = TypeVar("T", bound="Token")


class Maneuver(StateModel, Generic[T]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Gives details about a Token's journey along a path.

    Attributes:
        id: int
        token: T
        path: Path
        state: ManeuverState

    Provides:

    Super Class:
        Model
    """
    _id: int
    _token: T
    _path: Path
    _state: ManeuverState
    
    def __init__(
            self,
            id: int,
            token: T,
            path: Path,
    ):
        """
        Args:
            id: int
            token: T
            path: Path
        """
        self._token = token
        self._path = path
        self._id = id
        self._state = ManeuverState.NOT_COMPLETED
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def token(self) -> T:
        return self._token
    
    @property
    def path(self) -> Path:
        return self._path
    
    @property
    def state(self) -> ManeuverState:
        return self._state
    
    @state.setter
    def state(self, other: ManeuverState):
        self._state = other
    
    @property
    def is_completed(self) -> bool:
        return (
                self._path.endpoints.origin.occupant != self._token and
                self._path.endpoints.destination.occupant == self._token and
                self._state == ManeuverState.COMPLETED
        )
    
    @property
    def is_not_completed(self) -> bool:
        return not self.is_completed
    
    def __eq__(self, other):
        if other == self: return True
        if other is None: return False
        if isinstance(other, Maneuver):
            return (
                self._token == other.token and
                self.is_same_path(other)
            )
        return False
        
        
    def is_same_path(self, maneuver: Maneuver):
        return self._path == maneuver.path
        
    