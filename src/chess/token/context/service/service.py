# src/chess/piece/service/service.py

"""
Module: chess.piece.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""
from typing import cast

from chess.system import ContextService,  id_emitter
from chess.piece import PieceContext, PieceContextBuilder, PieceContextValidator, PieceFinder

class PieceContextService(ContextService[PieceContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facingPiece search microservice API.
    2.  Provides a map aware utility for searchingPiece objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth forPiece search results by having single entry and exit points for the
       Token search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *  PieceContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "PieceContextService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder:PieceFinder =PieceFinder(),
            builder:PieceContextBuilder =PieceContextBuilder(),
            validator:PieceContextValidator =PieceContextValidator(),
    ):
        """
        # Action:
        Constructor

        # Parameters:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (PieceFinder): Default value -PieceFinder()
            *   builder (PieceContextBuilder): Default value -PieceContextBuilder()
            *   validator (PieceContextValidator): Default value -PieceContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        method = "PieceContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) ->PieceFinder:
        """GetPieceFinder instance."""
        return cast(PieceFinder, self.entity_finder)
    
    @property
    def builder(self) ->PieceContextBuilder:
        """GetPieceContextBuilder instance."""
        return cast(PieceContextBuilder, self.entity_builder)
    
    @property
    def validator(self) ->PieceContextValidator:
        """GetPieceContextValidator instance."""
        return cast(PieceContextValidator, self.entity_validator)