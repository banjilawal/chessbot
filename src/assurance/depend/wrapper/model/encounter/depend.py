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
    ManeuverValidationServer, ParticipationValidationServer,
    SquareValidationServer, TokenValidationServer
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
    _token: TokenValidationServer
    _square: SquareValidationServer
    _maneuver: ManeuverValidationServer
    _participation: ParticipationValidationServer
    
    def __init__(
            self,
            token: Optional[TokenValidationServer] | None = None,
            square: Optional[SquareValidationServer] | None = None,
            maneuver: Optional[ManeuverValidationServer] | None = None,
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
        self._token = token or TokenValidationServer()
        self._square = square or SquareValidationServer()
        self._maneuver = maneuver or ManeuverValidationServer()
        self._participation = participation or ParticipationValidationServer()
        
    @property
    def token(self) -> TokenValidationServer:
        return self._token
    
    @property
    def square(self) -> SquareValidationServer:
        return self._square
    
    @property
    def maneuver(self) -> ManeuverValidationServer:
        return self._maneuver
    
    @property
    def participation(self) -> ParticipationValidationServer:
        return self._participation