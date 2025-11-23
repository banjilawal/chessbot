# src/chess/square/context/service/service.py

"""
Module: chess.square.context.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord, CoordService
from chess.system import BuildResult, IdentityService, Service
from chess.square import SquareContext, SquareContextBuilder, SquareContextValidator


class SquareContextService(Service[SquareContext]):
    """"""
    _builder: SquareContextBuilder
    _validator: SquareContextValidator
    
    def __init__(
            self,
            builder: SquareContextBuilder = SquareContextBuilder(),
            validator: SquareContextValidator = SquareContextValidator()
    ):
        """"""
        method = "SquareContextService.__init__"
        self._builder = builder
        self._validator = validator
        
    @property
    def validator(self) -> SquareContextValidator:
        """"""
        method = "SquareContextService.validator"
        return self._validator
    
    def build(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[SquareContext]:
        """"""
        method = "SquareContextService.builder"
        return self.builder.build(
            id=id,
            name=name,
            coord=coord,
            coord_service=coord_service,
            identity_service=identity_service
        )
        