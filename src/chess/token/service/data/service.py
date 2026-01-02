# src/chess/token/service/data/service_.py

"""
Module: chess.token.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult, id_emitter
from chess.token import Token, TokenContext, TokenDataServiceException, TokenFinder, TokenService, TokenContextService


class TokenDataService(DataService[Token]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Token objects and their lifecycles.
    3.  Ensure integrity of Token data stack
    4.  Stack data structure for Token objects with no guarantee of uniqueness.
    
    # PARENT:
        *   DataService[Token]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "TokenDataService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Token] = List[Token],
            service: TokenService = TokenService(),
            context_service: TokenContextService = TokenContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   items (List[Team])
            *   service (TeamService)
            *   context_service (TeamContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "TokenService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
        
    @property
    def token_service(self) -> TokenService:
        return cast(TokenService, self.entity_service)
    
    @property
    def token_context_service(self) -> TokenContextService:
        return cast(TokenContextService, self.context_service)

