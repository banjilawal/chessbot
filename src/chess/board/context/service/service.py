# src/chess/board/context/service/servicepy

"""
Module: chess.board.context.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import cast

from chess.system import ContextService, id_emitter
from chess.board import BoardContext, BoardContextBuilder, BoardContextValidator, BoardFinder


class BoardContextService(ContextService[BoardContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Board search microservice API.
    2.  Provides a map aware utility for searching Board objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Board search results by having single entry and exit points for the
        Board search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   BoardContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "BoardContextService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: BoardFinder = BoardFinder(),
            builder: BoardContextBuilder = BoardContextBuilder(),
            validator: BoardContextValidator = BoardContextValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   finder (BoardFinder)
            *   builder (BoardContextBuilder)
            *   validator (BoardContextValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "BoardContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> BoardFinder:
        """Get BoardFinder instance."""
        return cast(BoardFinder, self.entity_finder)
    
    @property
    def builder(self) -> BoardContextBuilder:
        """Get BoardContextBuilder instance."""
        return cast(BoardContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> BoardContextValidator:
        """Get BoardContextValidator instance."""
        return cast(BoardContextValidator, self.entity_validator)