# src/chess/piece/service/service.py

"""
Module: chess.piece.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""
from typing import cast

from chess.schema import SchemaService
from chess.system import ContextService,  id_emitter
from chess.token import TokenContext


class TokenContextService(ContextService[TokenContext]):
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
        *  TokenContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "TokenContextService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder:PieceFinder =PieceFinder(),
            schema_service: SchemaService = SchemaService(),
            builder:TokenContextBuilder =TokenContextBuilder(),
            validator:TokenContextValidator =TokenContextValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (PieceFinder): Default value -PieceFinder()
            *   builder (TokenContextBuilder): Default value -TokenContextBuilder()
            *   validator (TokenContextValidator): Default value -TokenContextValidator()

        # RETURNS:
        None

        # RAISES:
        None
        """
        method = "TokenContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) ->PieceFinder:
        """GetPieceFinder instance."""
        return cast(PieceFinder, self.entity_finder)
    
    @property
    def builder(self) ->TokenContextBuilder:
        """GetTokenContextBuilder instance."""
        return cast(TokenContextBuilder, self.entity_builder)
    
    @property
    def validator(self) ->TokenContextValidator:
        """GetTokenContextValidator instance."""
        return cast(TokenContextValidator, self.entity_validator)
    
    