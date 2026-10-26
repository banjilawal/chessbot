# src/assurance/depend/service/model/encounter/depend.py

"""
Module: assurance.depend.service.model.encounter.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Encounter
from exchange import (
    ManeuverValidationService, ParticipationValidationService,
    SquareValidationService, TokenValidationService
)


class EncounterDependency(ModelDependency[Encounter]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy EncounterValidator's ResponseService dependencies.

    Attributes:
        token: TokenValidationService
        square: SquareValidationService
        maneuver: ManeuverValidationService
        participation: ParticipationValidationService

    Provides:

    Super Class:
        ModelDependency
    """
    _token: TokenValidationService
    _square: SquareValidationService
    _maneuver: ManeuverValidationService
    _participation: ParticipationValidationService
    
    def __init__(
            self,
            token: Optional[TokenValidationService] | None = None,
            square: Optional[SquareValidationService] | None = None,
            maneuver: Optional[ManeuverValidationService] | None = None,
            participation: Optional[ParticipationValidationService]
                           | None = None,
    ):
        """
        Args:
            token: Optional[TokenValidationService]
            square: Optional[SquareValidationService]
            maneuver: Optional[ManeuverValidationService]
            participation: Optional[ParticipationValidationService]
        """
        super().__init__()
        self._token = token or TokenValidationService()
        self._square = square or SquareValidationService()
        self._maneuver = maneuver or ManeuverValidationService()
        self._participation = participation or ParticipationValidationService()
        
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
    def participation(self) -> ParticipationValidationService:
        return self._participation