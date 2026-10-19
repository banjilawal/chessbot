# src/assurance/depend/wrapper/model/encounter/depend.py

"""
Module: assurance.depend.wrapper.model.encounter.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Encounter
from exchange import (
    ManeuverValidationService, ParticipationValidationServer,
    SquareValidationService, TokenValidationService
)


class EncounterWrapperDependency(ModelWrapperDependency[Encounter]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy EncounterValidator's ResponseWrapper dependencies.

    Attributes:
        token: TokenValidationServer
        square: SquareValidationServer
        maneuver: ManeuverValidationServer
        participation: ParticipationValidationServer

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _token: TokenValidationService
    _square: SquareValidationService
    _maneuver: ManeuverValidationService
    _participation: ParticipationValidationServer
    
    def __init__(
            self,
            token: Optional[TokenValidationService] | None = None,
            square: Optional[SquareValidationService] | None = None,
            maneuver: Optional[ManeuverValidationService] | None = None,
            participation: Optional[ParticipationValidationServer]
                           | None = None,
    ):
        """
        Args:
            token: Optional[TokenValidationServer]
            square: Optional[SquareValidationServer]
            maneuver: Optional[ManeuverValidationServer]
            participation: Optional[ParticipationValidationServer]
        """
        super().__init__()
        self._token = token or TokenValidationService()
        self._square = square or SquareValidationService()
        self._maneuver = maneuver or ManeuverValidationService()
        self._participation = participation or ParticipationValidationServer()
        
    @property
    def token(self) -> TokenValidationService:
        return self._token
    
    @property
    def square(self) -> SquareValidationService:
        return self._square
    
    @property
    def maneuver(self) -> ManeuverValidationService:
        return self._maneuver
    
    @property
    def participation(self) -> ParticipationValidationServer:
        return self._participation