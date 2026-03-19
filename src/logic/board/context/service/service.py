# src/logic/board/context/service/servicepy

"""
Module: logic.board.context.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import cast

from logic.system import ContextService, id_emitter
from logic.board import BoardContext, BoardContextBuildProcess, BoardContextValidationProcess, BoardFinder


class BoardContextService(ContextService[BoardContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Board search microservice API.
    2.  Provides a map aware utility for searching Board objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Board search results by having single entry and exit points for the
        Board search flow.

    Super Class:
        *   ContextService

    # PROVIDES:
        *   BoardContextService


    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "BoardContextService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: BoardFinder = BoardFinder(),
            builder: BoardContextBuildProcess = BoardContextBuildProcess(),
            validator: BoardContextValidationProcess = BoardContextValidationProcess(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   finder (BoardFinder)
            *   builder (BoardContextBuildProcess)
            *   validator (BoardContextValidationProcess)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "BoardContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> BoardFinder:
        """Get BoardFinder instance."""
        return cast(BoardFinder, self.entity_finder)
    
    @property
    def build(self) -> BoardContextBuildProcess:
        """Get BoardContextBuildProcess instance."""
        return cast(BoardContextBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> BoardContextValidationProcess:
        """Get BoardContextValidationProcess instance."""
        return cast(BoardContextValidationProcess, self.entity_validator)