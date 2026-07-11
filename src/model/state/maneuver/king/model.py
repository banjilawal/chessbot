# src/model/state/maneuver/king/model.py

"""
Module: model.state.maneuver.king.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import King, KingManeuverWarning, KingToken, Maneuver, Path


class KingManeuver(Maneuver[King]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide information about a path a KingToken might follow.

    Attributes:
        king: KingToken
        maneuver_warning: KingManeuverWarning

    Provides:

    Super Class:
        Path
    """
    _maneuver_warning: KingManeuverWarning
    
    def __init__(
            self,
            id: int,
            path: Path,
            king: KingToken,
    ):
        """
        Args:
            id: int
            path: Path
            king: KingToken
        """
        super().__init__(id=id, token=king, path=path)
        self._maneuver_warning = KingManeuverWarning.DESTINATION_IS_SAFE
    

    @property
    def king(self) -> KingToken:
        return cast(KingToken, self.token)
    
    @property
    def maneuver_warning(self) -> KingManeuverWarning:
        return self._maneuver_warning
    
    @property
    def is_checked(self) -> bool:
        return (
                self.is_completed and
                self.maneuver_warning == KingManeuverWarning.DESTINATION_UNDER_CHECK
        )
    
    @property
    def is_not_checked(self) -> bool:
        return not self.is_checked
    
    @maneuver_warning.setter
    def maneuver_warning(self, other: KingManeuverWarning):
        self._maneuver_warning = other
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, KingManeuver):
            return super().__eq__(other)
        return False
    
    def __hash__(self):
        return super.__hash__(self)