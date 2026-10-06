# src/assurance/depend/wrapper/model/encounter/depend.py

"""
Module: assurance.depend.wrapper.model.encounter.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Any, Optional, SupportsIndex

from assurance import ModelWrapperDependency
from domain import Encounter
from exchange import (
    ManeuverValidationResponseWrapper, ParticipationValidationResponseWrapper,
    TokenValidationResponseWrapper
)


class EncounterWrapperDependency(ModelWrapperDependency[Encounter]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy EncounterValidator's ResponseWrapper dependencies.

    Attributes:
        token: TokenValidationResponseWrapper
        maneuver: ManeuverValidationResponseWrapper
        participation: ParticipationValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _token: TokenValidationResponseWrapper
    _maneuver: ManeuverValidationResponseWrapper
    _participation: ParticipationValidationResponseWrapper
    
    def __init__(
            self,
            token: Optional[TokenValidationResponseWrapper] | None = None,
            maneuver: Optional[ManeuverValidationResponseWrapper] | None = None,
            participation: Optional[ParticipationValidationResponseWrapper]
                           | None = None,
    ):
        """
        Args:
            token: Optional[TokenValidationResponseWrapper]
            maneuver: Optional[ManeuverValidationResponseWrapper]
            participation: Optional[ParticipationValidationResponseWrapper]
        """
        super().__init__()
        self._token = token or TokenValidationResponseWrapper()
        self._maneuver = maneuver or ManeuverValidationResponseWrapper()
        self._participation = participation or ParticipationValidationResponseWrapper()
        
    @property
    def token(self) -> TokenValidationResponseWrapper:
        return self._token
    
    @property
    def maneuver(self) -> ManeuverValidationResponseWrapper:
        return self._maneuver
    
    @property
    def participation(self) -> ParticipationValidationResponseWrapper:
        return self._participation