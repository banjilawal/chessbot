# src/model/state/maneuver/combatant/model.py

"""
Module: model.state.maneuver.combatant.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import CombatantManeuverWarning, CombatantToken, Maneuver, Path


class CombatantManeuver(Maneuver[CombatantToken]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide information about a path a CombatantToken might follow.

    Attributes:
        combatant: CombatantToken
        maneuver_warning: CombatantManeuverWarning

    Provides:

    Super Class:
        Path
    """
    _maneuver_warning: CombatantManeuverWarning
    
    def __init__(
            self,
            id: int,
            path: Path,
            combatant: CombatantToken,
    ):
        """
        Args:
            id: int
            path: Path
            combatant: CombatantToken
        """
        super().__init__(id=id, token=combatant, path=path)
        self._maneuver_warning = CombatantManeuverWarning.DESTINATION_IS_SAFE
    

    @property
    def combatant(self) -> CombatantToken:
        return cast(CombatantToken, self.token)
    
    @property
    def maneuver_warning(self) -> CombatantManeuverWarning:
        return self._maneuver_warning
    
    @property
    def is_vulnerable(self) -> bool:
        return (
                self.is_completed and
                self.maneuver_warning == CombatantManeuverWarning.VULNERABLE_DESTINATION
        )
    
    @property
    def is_not_vulnerable(self) -> bool:
        return not self.is_vulnerable
    
    @maneuver_warning.setter
    def maneuver_warning(self, other: CombatantManeuverWarning):
        self._maneuver_warning = other
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, CombatantManeuver):
            return super().__eq__(other)
        return False
    
    def __hash__(self):
        return super.__hash__(self)