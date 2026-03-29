# src/logic/board/query/service/servicepy

"""
Module: logic.board.query.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import cast

from logic.system import QueryService, id_emitter
from logic.board import BoardContext, BoardContextBuilder, BoardContextValidationTransaction, BoardFinder


class BoardQueryService(QueryService[BoardContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Board search microservice API.
    2.  Provides a map aware utility for searching Board objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Board search results by having single entry and exit points for the
        Board search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *   BoardQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "BoardQueryService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: BoardFinder = BoardFinder(),
            builder: BoardContextBuilder = BoardContextBuilder(),
            validator: BoardContextValidationTransaction = BoardContextValidationTransaction(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   route (BoardFinder)
            *   build (BoardContextBuilder)
            *   validation (BoardContextValidationTransaction)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "BoardQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> BoardFinder:
        """Get BoardFinder instance."""
        return cast(BoardFinder, self.entity_finder)
    
    @property
    def build(self) -> BoardContextBuilder:
        """Get BoardContextBuilder instance."""
        return cast(BoardContextBuilder, self.entity_builder)
    
    @property
    def validation(self) -> BoardContextValidationTransaction:
        """Get BoardContextValidationTransaction instance."""
        return cast(BoardContextValidationTransaction, self.entity_validator)