# src/domain/metadata/blueprint/model/state/encounter/warnining/plueprint.py

"""
Module: domain.metadata.blueprint.model.state.encounter.warning.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import (
    EncounterBlueprint, EncounterWarning, KingToken, Maneuver, Square
)
from err import EncounterWarningNullException


class EncounterWarningBlueprint(EncounterBlueprint[EncounterWarning]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating an EncounterWarning object.

     Attributes:
        maneuver: Maneuver
        warning_recipient: KingToken
        current_safe_square: Square
        danger_zone: Optional[Square]
        attacker_reward: Optional[int]
        
        domain_class: Optional[Type[EncounterWarning]]
        domain_null_exception: Optional[EncounterWarningNullException]

     Provides:

     Super Class:
        EncounterBlueprint
     """
    _current_safe_square: Square
    _danger_zone: Optional[Square]
    
    def __init__(
            self,
            attacker_maneuver: Maneuver,
            warning_recipient: KingToken,
            current_safe_square: Square,
            domain_class: Optional[Type[EncounterWarning]] | None = None,
            domain_null_exception: Optional[EncounterWarningNullException] | None = None,
            danger_zone: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            attacker_maneuver: Maneuver
            warning_recipient: KingToken
            current_safe_square: Square
            domain_class: Optional[Type[EncounterWarning]]
            domain_null_exception: Optional[EncounterWarningNullException]
            danger_zone: Optional[Square]
            attacker_reward: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            victim=warning_recipient,
            attacker_maneuver=attacker_maneuver,
            location=danger_zone,
            attacker_reward=attacker_reward or warning_recipient.rank.ransom,
            domain_class=domain_class or EncounterWarning,
            domain_null_exception=domain_null_exception or EncounterWarningNullException(),
        )
        self._current_safe_square = current_safe_square
        self._danger_zone = danger_zone
    
    @property
    def current_safe_square(self) -> Square:
        return self._current_safe_square
    
    @property
    def warning_recipient(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.warning_recipient
    
    @property
    def danger_zone(self) -> Optional[Square]:
        return self._danger_zone
    
    @property
    def domain_class(self) -> Type[EncounterWarning]:
        return cast(Type[EncounterWarning], super().domain_class)
    
    @property
    def domain_null_exception(self) -> EncounterWarningNullException:
        return cast(EncounterWarningNullException, super().domain_null_exception)




    
    

        
        